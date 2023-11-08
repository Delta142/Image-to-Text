from tkinter import *
import tkinter as tk
from tkinter import filedialog

from PIL import ImageTk, Image
from os import listdir, path
from Tools import ImageToTextWithTesseract as ImTeTs

#becarefull of the Globals:
#download TKInter
'''
    global PictureHolder
'''

DEV = False
APP_LENGTH = 6
APP_HEIGHT = 13
TASKS_BAR = 0
TASK_ROW = 1 
WORK_COLUMN = 1
IMAGE_ROW = 1
IMAGE_OUT_ROW = IMAGE_ROW + 9
CANVAS_SIZE = 400

BK_G_DEF = "lightblue"
BUTTN_COLLOR = "cadetblue"
TITLE_COLLOR = "Black"
LABEL_COLLOR = "darkturquoise"
WARNING_COLLOR = BK_G_DEF

main_window = Tk()

#configure window
main_window.geometry("700x700")
main_window.title("Image Reader 9000")
main_window.configure(background=BK_G_DEF)

#Create Padds
for i in range(APP_HEIGHT):
    for j in range(APP_LENGTH):
        if (DEV):
            cell = Frame(main_window, width=100, height=50, background="Blue")
        else:
            cell = Frame(main_window, width=100, height=50, background=BK_G_DEF)
        cell.grid(row=i, column=j, padx=1,pady=1)

#Header
Label(main_window, text="Welcome To text Reader 9000",background=TITLE_COLLOR,foreground="White").grid(row=0,column=0,columnspan=APP_LENGTH)

#work Image Container
CanvasContainer = Canvas(main_window, width=400, height=400, background="gray")
CanvasContainer.grid(row=IMAGE_ROW,column=WORK_COLUMN, rowspan=8,columnspan=4)
Work_Image_Prev = Image.open("Figures/Logo.png")
Work_Image_Prev = Work_Image_Prev.resize((300, 300),Image.LANCZOS)
Work_Image=ImageTk.PhotoImage(Work_Image_Prev)
Image_Container = CanvasContainer.create_image(200,200,image=Work_Image)

#image field
Label(main_window, text="Image location:",background=LABEL_COLLOR).grid(row=IMAGE_ROW+8,column=WORK_COLUMN)
ImageLocation = Entry(main_window,borderwidth=2)
ImageLocation.grid(row=IMAGE_ROW+8,column=WORK_COLUMN+1,columnspan=2)

#image output field
Image_Location_warining = Label(main_window, text="", background=WARNING_COLLOR, foreground="red")
Image_Location_warining.grid(row=IMAGE_OUT_ROW,column=WORK_COLUMN, columnspan=4)
ImageOut = Text(main_window, width=50,height=7, borderwidth=2)
ImageOut.grid(row=IMAGE_OUT_ROW+1, column=WORK_COLUMN, columnspan=4,rowspan=3)
#functions
def ChangeImage():
    global PictureHolder
    
    #Checking Input
    PreviewImageLocation=str(ImageLocation.get())
    if( not path.isfile(PreviewImageLocation)):
        print(f"This is a not path to a file{str(PreviewImageLocation)}")
        PreviewImageLocation = ""
    else:
        Image_Location_warining.config(text=f"")
    
    if(PreviewImageLocation == ""):
        Image_Location_warining.config(text=f"path to '{ImageLocation.get()}' not found")
        PreviewImageLocation = "./Train_data/text/sampletext.png"
    ImageLocation.delete(0,END)
    ImageLocation.insert(0,PreviewImageLocation)
    
    #gathering data
    Work_Image_Prev = Image.open(PreviewImageLocation)
    (width, height) = (Work_Image_Prev.width, Work_Image_Prev.height)
    if(width > height):
        Ratio = CANVAS_SIZE/width
    else:
        Ratio = CANVAS_SIZE/height
    
    NewSize = (int(width*Ratio), int(height*Ratio))
    PictureHolder = ImageTk.PhotoImage(Work_Image_Prev.resize(NewSize))
    Work_Image_Prev.close()
    CanvasContainer.itemconfig(Image_Container,image=PictureHolder)


def WordScanner():
    #checks
    PreviewImageLocation=str(ImageLocation.get())
    if( not path.isfile(PreviewImageLocation)):
        print(f"This is a not path to a file{str(PreviewImageLocation)}")
        return

    TextFound = ImTeTs.getImageText(ImageLocation.get())
    ImageOut.delete(1.0,"end")
    ImageOut.insert("end", f"{TextFound}")

    
def browseFiles():
    filePath = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("PNG files", "*.png*"), ("all files", "*.*")))
    ImageLocation.insert(tk.END, filePath)

def Text2Speech():
    pass

def SaveIMG():
    #save to History
    ImTeTs.saveImageText(pathUsed=ImageLocation.get(), textGenerated=ImageOut.get("1.0",END))
    #save to independent file
    ImTeTs.saveImageTextSingle(pathUsed=ImageLocation.get(), textGenerated=ImageOut.get("1.0", END))

def PlaceHolder():
    pass
#buttons
Button(main_window, text="Update Image",command=ChangeImage,background=BUTTN_COLLOR).grid(row=IMAGE_ROW+8,column=WORK_COLUMN+3)

# Actions
Label(main_window, text="Try our Image Analysis options", background=LABEL_COLLOR).grid(row=TASK_ROW,column=TASKS_BAR)
Button(main_window, text="Word Scanner",command=WordScanner,background=BUTTN_COLLOR).grid(row=TASK_ROW+1,column=TASKS_BAR)
Button(main_window, text="Text 2 speach",command=PlaceHolder,background=BUTTN_COLLOR).grid(row=TASK_ROW+2,column=TASKS_BAR)
Button(main_window, text="Place Holder",command=PlaceHolder,background=BUTTN_COLLOR).grid(row=TASK_ROW+3,column=TASKS_BAR)
Button(main_window, text="Place Holder",command=PlaceHolder,background=BUTTN_COLLOR).grid(row=TASK_ROW+4,column=TASKS_BAR)

Button(main_window, text="Save Text",command=SaveIMG,background=BUTTN_COLLOR).grid(row=IMAGE_ROW+9,column=WORK_COLUMN)
Button(main_window, text="Browse Files",command=browseFiles,background=BUTTN_COLLOR).grid(row=IMAGE_ROW+9,column=WORK_COLUMN+3)

main_window.mainloop()
