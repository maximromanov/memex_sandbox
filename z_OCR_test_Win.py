import pytesseract
import os

image = "./_misc/sample.png"
image = "Z:/Dropbox/6.Teaching_New/BUILDING_MEMEX_COURSE/_memex_sandbox/_misc/sample.png"
#text = pytesseract.image_to_string(image, lang="eng")

print(os.path.isfile(image))

#print("="*80)
#print(text)
#print("="*80)