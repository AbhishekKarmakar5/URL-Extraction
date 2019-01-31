from PIL import Image
import pytesseract
import cv2
import re
import os
import webbrowser

img=cv2.imread("Testing.png")

#conversion of the image into gray
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#file has been created to be fed into the tesseract engine
file="{}.png" .format(os.getpid())

#writing the file to the disk
cv2.imwrite(file,gray)

#FEEDING-so the string would be returned to the tesseract engine
text=pytesseract.image_to_string(Image.open(file))

#removal of the file as it's no longer needed
os.remove(file)

print(text)

#finding the URL in the text and extracting it using regular expression
urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[.]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)

#Since there is only one URL is present so it gets saved in the array[0] i.e. urls[0]
print(urls[0])

webbrowser.open(urls[0])
