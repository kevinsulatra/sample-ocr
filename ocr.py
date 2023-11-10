# sudo apt-get install tesseract-ocr
# sudo apt-get install libtesseract-dev
# pip install pytesseract pillow


from PIL import Image
import pytesseract

# Path to the Tesseract executable (you may not need to set this explicitly on Ubuntu)
# pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Open an image file using PIL (Pillow)
image_path = 'example_image.png'
image = Image.open(image_path)

# Use Tesseract to do OCR on the image
text = pytesseract.image_to_string(image)

# Print the extracted text
print("Extracted Text:")
print(text)
