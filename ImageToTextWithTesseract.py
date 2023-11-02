#Image to text
import pytesseract
#Image processing
from PIL import Image

#Open image
Image = Image.open("text12.png")

#Image
print("Image info: ")
print(Image)
print("\n")

#Access tesseract
pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract.exe'

#Convert Image to Text
Text = pytesseract.image_to_string(Image)

#Output Text
print("Output from image: ")
print(Text)

#Storing test scans
file=open("TestStorage.txt","a")
file.write("Output of test:\n")
file.write(Text)
file.write("\n")
file.close()
