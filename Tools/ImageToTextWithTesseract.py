#Image to text
import pytesseract
#Image processing
from PIL import Image
import os

def getImageText(pathUsed="./Train_data/text/sampletext.png"):
    #Open image
    Img = Image.open(pathUsed)

    #Image
    print("Image info: ")
    print(Img)
    print("\n")

    #Access tesseract
    pytesseract.pytesseract.tesseract_cmd ='c:\Program Files\Tesseract-OCR\\tesseract.exe'

    #Convert Image to Text
    Text = pytesseract.image_to_string(Img)

    #Output Text
    #print("Output from image: ")
    #print(Text)
    '''    
    #Storing test scans
    file=open("TestStorage.txt","a")
    file.write("Output of test:\n")
    file.write(Text)
    file.write("\n")
    file.close()
    '''
    return Text

def saveImageText(pathUsed="TextSaved.txt", textGenerated="Information Lost..."):
    file=open(pathUsed,"a")
    file.write(textGenerated)
    file.write("\n")
    file.close()

def saveImageTextSingle(pathUsed="/Null/NoName.png", textGenerated="Picture Was Empty"):
    pass