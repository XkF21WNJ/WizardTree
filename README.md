# WizardTree

## XiuathoTheWizard's tale
- [Static version](https://XkF21WNJ.github.io/WizardTree/)
- [Dynamic version](https://XkF21WNJ.github.io/WizardTree/Viewer.html)

## Project Description and History

The goal of this project is to convert 'choose your own adventure style' comment chains that sometimes appear on reddit (e.g. /r/ playzorkwithme and /r/YouEnterADungeon) into easier to handle formats.

The motivation behind this project was the tale of /u/XiuathoTheWizard, which spontaneously grew from [this comment](https://www.reddit.com/r/talesfromtechsupport/comments/3xyesc/project_management_seems_a_lot_like_cooking_a/cy8z5uv) on the subreddit /r/TalesFromTechSupport.  Since it is hard to navigate comment chains of that size on reddit this project was started to attempt compile the tale it into a more manageable format.

Current formats include .html and .json, but other formats should be possible, and can hopefully be added soon.

## Instructions

Currently most functionality can be found in the 'WizardCrawler.ipynb' file. To run this file you'll need a python distribution (2.7, although 3+ might also work). And to open the notebook you'll need to use the [Jupyter](http://jupyter.org/) package. 

The code also requires some other python packages, depending on what part of the code you'll want to use. Currently used packages include: praw, html, json, markdown.

The generated .json files contain a list of all events and possible actions indexed by their comment id. This layout makes it easy to generate choose your own adventure style stories in various formats. As an example 'WizardCrawler.ipynb' can convert the json file to a single fixed html, and 'Viewer.html' canget a similar result by loading the json directly in the browser.

## Goals

For now the main goal is to make the code more general, allowing it to be used to (easily) crawl other stories and convert them into manageable formats. Some changes to the json format might be required (like the one made recently) but the current format does seem the simplest to work with, so no big changes are to be expected (though I might decide that it's better to store the text in markdown rather than html, but I'm not yet sure; the current viewer needs html).

Apart from that it would also be nice to have a broader range of formats and to improve upon the currently available ones (better styling / more functionality). Some candidates for new formats are:

- Epub  
This would basically just be an extension of the currently available html version, adding whatever information epubs need and repackaging it into the right format. Since epubs are essentially html files in a zip file this should be relatively easy to do (famous last words). Once this is available the static html format can be deprecated, the dynamic html viewer is more flexible and epubs are better as a static format.

- [Twine](http://twinery.org/)  
I've only encountered this recently but the language does seem to add support for scripting so with any luck it's possible to make it load the .json file directly, similar to how the currently available [html viewer](https://XkF21WNJ.github.io/WizardTree/Viewer.html) does it.

- Pdf  
Not yet sure how to generate Pdf's from json files, but it's technically possible. Maybe there's a python package that can be used for that. Of course, things like epubs and html files can be converted to pdf, but it's usually better to generate them directly.

## Contributing

Yes please! Just fork the repository and add a pull request to merge your changes. The project has only just started, and there are lots of things that could be improved, so any help is appreciated.

## Credits

Thanks to /u/XiuathoTheWizard and everyone else who contributed to his story. 

Code by /u/XkF21WNJ.

## License

All code is released under the MIT license. 

Files containing part or all of /u/XiuathoTheWizard's comments are published with permission, but otherwise all rights are reserved.
