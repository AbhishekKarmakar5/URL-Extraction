Extract URL links from images using OCR in python.

pillow module has been used for image handling

pytesseract module has been used to provide interface for tesseract engine but firstly the tesseract file shoud be installed already

os module helps to create temporary file which would be feeded to the tesseract engine

re module is for regular expression and is used here for URL finding

webbrowser module automatically opens up the browser, so that makes the searching of the URL becomes easier.
