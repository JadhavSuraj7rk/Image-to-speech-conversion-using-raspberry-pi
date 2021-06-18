from PIL import Image
import pytesseract


def image_to_text():

    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    image = Image.open('E:/Image/sample1.jpg')

    text = pytesseract.image_to_string(image, lang='eng')

    with open('sample.txt', mode='w') as file:
        file.write(text)
        print(text)
