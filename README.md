# WizardTree

## XiuathoTheWizard's tale
- [Static version](https://XkF21WNJ.github.io/WizardTree/)
- [Dynamic version](https://XkF21WNJ.github.io/WizardTree/Viewer.html)

## Project Description and History

The goal of this project is to convert 'choose your own adventure'-style comment chains that sometimes appear on reddit (such as on /r/playzorkwithme and /r/YouEnterADungeon) into easier to handle formats.

The inspiration for this project was the tale of /u/XiuathoTheWizard, which spontaneously grew from [this comment](https://www.reddit.com/r/talesfromtechsupport/comments/3xyesc/project_management_seems_a_lot_like_cooking_a/cy8z5uv) on the subreddit /r/TalesFromTechSupport.  Since it is hard to navigate comment chains of that size on reddit this project was started to compile the tale it into a more manageable format.

Current formats include HTML and JSON, but other formats should be possible, and can hopefully be added soon.

## Instructions

For a basic tutorial see the "tutorial.ipynb" file. To run the notebook you'll need to use the [Jupyter](http://jupyter.org/) package, but you can also copy the python code and run it directly.

The generated JSON files contain a list of all events and possible actions indexed by their comment id. This layout makes it easy to generate 'choose your own adventure'-style stories in various formats. For example 'WizardCrawler.ipynb' can convert the JSON file to a stand-alone HTML file, and 'Viewer.html' can be used to get a similar result by loading the JSON directly in the browser.

## Goals

For now the main goal is to make the code more general, allowing it to be used to (easily) crawl other stories and convert them into manageable formats. Some changes to the JSON format might be required (like the one made recently) but the current format does seem the simplest to work with, so no big changes are to be expected (though I might decide that it's better to store the text in markdown rather than HTML, but I'm not yet sure; the current viewer needs HTML).

Apart from that it would also be nice to have a broader range of formats and to improve upon the currently available ones (better styling / more functionality). Some candidates for new formats are:

- Epub  
This would basically just be an extension of the currently available HTML version, adding whatever information epubs need and repackaging it into the right format. Since epubs are essentially HTML files in a zip file this should be relatively easy to do (famous last words). Once this is available the static HTML format can be deprecated, the dynamic HTML viewer is more flexible and epubs are better as a static format.

- [Twine](http://twinery.org/)  
Haven't had much experience with this language but they do claim to add support for scripting so with any luck it's possible to make it load the JSON file directly, similar to how the currently available [HTML viewer](https://XkF21WNJ.github.io/WizardTree/Viewer.html) does it.

- Pdf  
Not yet sure how to generate Pdf's from JSON files, but it's technically possible. Maybe there's a python package that can be used for that. Of course, things like epubs and HTML files can be converted to pdf, but it's usually better to generate them directly.

## Contributing

Yes please! Just fork the repository and add a pull request to merge your changes. The project has only just started, and there are lots of things that could be improved, so all help is appreciated.

## Credits

Thanks to /u/XiuathoTheWizard and everyone else who contributed to his story. 

Code by /u/XkF21WNJ.

## License

All code is released under the MIT license. 

Files containing part or all of /u/XiuathoTheWizard's comments are published with permission, but otherwise all rights are reserved.
