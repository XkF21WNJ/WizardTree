#Imports
import praw
import markdown as md
import json

#Definitions
def YieldAll(comments):
    for c in comments:
        if isinstance(c, praw.objects.MoreComments):
            for x in YieldAll(c.comments()): yield x
        else: yield c

def IsWizard(story, comment):
    return str(comment.author) == story['author']

def FindWizard(story, comments):
    for c in YieldAll(comments):
        if IsWizard(story, c): yield c
    
def ParseSubmission(story, submission):
    story['events'][submission.id] = {"description": md.markdown(submission.body), 
                                      "actions" : list(ParseReplies(story, submission.comments, submission.id)),
                                      "parent" : None,
                                      "url" : submission.url}
    return submission.id

def ParseComment(story, comment, parent):
    story['events'][comment.id] = {"description": md.markdown(comment.body), 
                                   "actions" : list(ParseReplies(story, comment.replies, comment.id)),
                                   "parent" : parent,
                                   "url" : comment.permalink}
    return comment.id

def ParseReplies(story, comments, parent):
    for r in YieldAll(comments):
        consequence = FindConsequence(story, r.replies, parent)
        if consequence == None: continue;
        story['actions'][r.id] = {"description": md.markdown(r.body),
                                  "consequence" : consequence,
                                  "actor" : r.author.name,
                                  "url" : r.permalink}
        story['actors'].append(r.author.name)
        yield r.id;
        
def FindConsequence(story, comments, parent):
    for c in FindWizard(story, comments):
        return ParseComment(story, c, parent)
        
def Crawl(content):    
    if isinstance(content, praw.objects.Submission):
        story = {'author' : content.author.name,
                 'url' : content.url,
                 'start' : content.id,
                 'title': content.title}
    elif isinstance(content, praw.objects.Comment):
        story = {'author' : content.author.name,
                 'url' : content.permalink,
                 'start' : content.id,
                 'title' : content.submission.title}
    
    story['events'] = {}
    story['actions'] = {}
    story['actors'] = []

    if isinstance(content, praw.objects.Submission):
        ParseSubmission(story, content)
    elif isinstance(content, praw.objects.Comment):
        ParseComment(story, content, None)
    
    #Finalize
    uniq_actors = list(set(story['actors']))
    uniq_actors.sort(key = story['actors'].count, reverse = True)
    story['actors'] = uniq_actors
    
    return story

def CrawlSubmission(url = None, submission_id = None):
    r = praw.Reddit(user_agent='WizardCrawler/0.1 (by /u/XkF21WNJ)')
    
    if (url != None):
        submission = r.get_submission(url=url)
    elif (submission_id != None):
        submission = r.get_submission(submission_id=submission_id)
    
    return Crawl(submission)

def CrawlComment(url = None, comment_id = None):
    r = praw.Reddit(user_agent='WizardCrawler/0.1 (by /u/XkF21WNJ)')

    if (url != None):
        comment = r.get_submission(url=url).comments[0]
    elif (comment_id != None):
        comment = r.get_info(thing_id = "t1_"+comment_id)
        comment.refresh()
  
    return Crawl(comment)

def Import(filename):
    with open(filename,'r') as f:
        return json.load(f)

def Export(story, filename):
    with open(filename,'w') as f:
        json.dump(story, f, indent=4)