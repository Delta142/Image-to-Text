#Image to text
import pytesseract
#Image processing
from PIL import Image
import os
import time

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

def saveImageText(savedPath="Scanned_History.txt", pathUsed="NotFound", textGenerated="Information Lost..."):
    file=open(savedPath,"a")
    file.write(f'Time Scanned: {time.ctime()}\nFile Scanned: [{pathUsed}]\n')
    file.write(f'-----------------------------------------------------------------\n')
    file.write(textGenerated)
    file.write(f'-----------------------------------------------------------------\n')
    file.write("\n")
    file.close()

def saveImageTextSingle(pathUsed="/Null/NoName.png", textGenerated="Picture Was Empty"):
    Pathsplit = pathUsed.split('/')
    FileName = (Pathsplit[-1]).split('.')

    file=open(FileName[0],"w")
    file.write(textGenerated)
    file.close()
