from PIL import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image = Image.open('E:/Image/sample1.jpg')

image_to_text = pytesseract.image_to_string(image, lang='eng')

# print(image_to_text)

with open('sample.txt', mode='w') as file:
    file.write(image_to_text)
    print(image_to_text)
