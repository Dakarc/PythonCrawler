import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'D:\TesseractOCR\tesseract.exe'

image = Image.open("2.png")

text = pytesseract.image_to_string(image,lang='chi_sim')

print(text)