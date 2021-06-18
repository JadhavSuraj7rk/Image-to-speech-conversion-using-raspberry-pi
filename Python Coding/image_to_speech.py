from PIL import Image
from gtts import gTTS
import pytesseract
import os
import time


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image = Image.open('E:/Image/sample1.jpg')

image_to_text = pytesseract.image_to_string(image, lang='eng')

# print(image_to_text)

with open('sample.txt', mode='w') as file:
    file.write(image_to_text)
    print(image_to_text)

# time.sleep(10)
fh = open("sample.txt", "r")
Text = fh.read()

language = 'en'

output = gTTS(text=Text, lang=language, slow=False)

output.save("sample.mp3")
fh.close()
os.system("start sample.mp3")
