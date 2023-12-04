#For: GUI
from tkinter import * 
import tkinter as tk
from tkinter import filedialog, font, W
#For: Image to text converter, ...
from PIL import ImageTk, Image
from os import listdir, path
import ImageToTextWithTesseract as ImTeTs
#For: Text to speech
import pyttsx3
#For: Translate to different Language
#import translateText as trText
from translate import Translator

#be careful of the Globals:
#download TKInter
'''
    global PictureHolder
'''

# ...
DEV = False
WORK_COLUMN = 1
IMAGE_ROW = 1

#colors of interface
BK_G_DEF = '#36454F' #Originally "lightblue"
BUTTN_COLOR = "cadetblue"
LABEL_COLOR = "cyan" #Originally "darkblue"
SavedText = ""
languages = [
    ("Afrikaans", "af"),
    ("Albanian", "sq"),
    ("Amharic", "am"),
    ("Arabic", "ar"),
    ("Armenian", "hy"),
    ("Azerbaijani", "az"),
    ("Basque", "eu"),
    ("Belarusian", "be"),
    ("Bengali", "bn"),
    ("Bosnian", "bs"),
    ("Bulgarian", "bg"),
    ("Catalan", "ca"),
    ("Cebuano", "ceb"),
    ("Chinese (Simplified)", "zh-CN"),
    ("Chinese (Traditional)", "zh-TW"),
    ("Corsican", "co"),
    ("Croatian", "hr"),
    ("Czech", "cs"),
    ("Danish", "da"),
    ("Dutch", "nl"),
    ("English", "en"),
    ("Esperanto", "eo"),
    ("Estonian", "et"),
    ("Finnish", "fi"),
    ("French", "fr"),
    ("Frisian", "fy"),
    ("Galician", "gl"),
    ("Georgian", "ka"),
    ("German", "de"),
    ("Greek", "el"),
    ("Gujarati", "gu"),
    ("Haitian Creole", "ht"),
    ("Hausa", "ha"),
    ("Hawaiian", "haw"),
    ("Hebrew", "he"),
    ("Hindi", "hi"),
    ("Hmong", "hmn"),
    ("Hungarian", "hu"),
    ("Icelandic", "is"),
    ("Igbo", "ig"),
    ("Indonesian", "id"),
    ("Irish", "ga"),
    ("Italian", "it"),
    ("Japanese", "ja"),
    ("Javanese", "jv"),
    ("Kannada", "kn"),
    ("Kazakh", "kk"),
    ("Khmer", "km"),
    ("Kinyarwanda", "rw"),
    ("Korean", "ko"),
    ("Kurdish (Kurmanji)", "ku"),
    ("Kyrgyz", "ky"),
    ("Lao", "lo"),
    ("Latin", "la"),
    ("Latvian", "lv"),
    ("Lithuanian", "lt"),
    ("Luxembourgish", "lb"),
    ("Macedonian", "mk"),
    ("Malagasy", "mg"),
    ("Malay", "ms"),
    ("Malayalam", "ml"),
    ("Maltese", "mt"),
    ("Maori", "mi"),
    ("Marathi", "mr"),
    ("Mongolian", "mn"),
    ("Myanmar (Burmese)", "my"),
    ("Nepali", "ne"),
    ("Norwegian", "no"),
    ("Odia (Oriya)", "or"),
    ("Pashto", "ps"),
    ("Persian", "fa"),
    ("Polish", "pl"),
    ("Portuguese", "pt"),
    ("Punjabi", "pa"),
    ("Romanian", "ro"),
    ("Russian", "ru"),
    ("Samoan", "sm"),
    ("Scots Gaelic", "gd"),
    ("Serbian", "sr"),
    ("Sesotho", "st"),
    ("Shona", "sn"),
    ("Sindhi", "sd"),
    ("Sinhala", "si"),
    ("Slovak", "sk"),
    ("Slovenian", "sl"),
    ("Somali", "so"),
    ("Spanish", "es"),
    ("Sundanese", "su"),
    ("Swahili", "sw"),
    ("Swedish", "sv"),
    ("Tajik", "tg"),
    ("Tamil", "ta"),
    ("Tatar", "tt"),
    ("Telugu", "te"),
    ("Thai", "th"),
    ("Turkish", "tr"),
    ("Turkmen", "tk"),
    ("Ukrainian", "uk"),
    ("Urdu", "ur"),
    ("Uyghur", "ug"),
    ("Uzbek", "uz"),
    ("Vietnamese", "vi"),
    ("Welsh", "cy"),
    ("Xhosa", "xh"),
    ("Yiddish", "yi"),
    ("Yoruba", "yo"),
    ("Zulu", "zu")
]

#create window
main_window = Tk()

#configure window
main_window.geometry("1400x900") # dimension # dimension
main_window.title("Image Reader 9000") # title
main_window.configure(background = BK_G_DEF) # background color

#Generate cells of GUI
for i in range(30): #30 Cells in Width 
    for j in range(20): #20 Cells in Height

        if (DEV):
            cell = Frame(main_window, width = 200, height = 35, background= "Blue")
        else:
            cell = Frame(main_window, width = 200, height = 35, background = BK_G_DEF) # BK_G_DEF

        cell.grid(row = i, column = j, padx = 1, pady = 1)

#Work Image Container
CanvasContainer = Canvas(main_window, width = 600, height = 545, background="white", highlightbackground="black", highlightthickness = 1) #Creates widget with set width and height in pixels, and color
CanvasContainer.grid(row = IMAGE_ROW+1, column = WORK_COLUMN-1, rowspan = 17, columnspan = 4) #Places widget in cells
Work_Image_Prev = Image.open("InsertHere.jpeg") #Opens default image file
Work_Image_Prev = Work_Image_Prev.resize((425, 425), Image.LANCZOS) #Resizes image using LANCZOS filter
Work_Image = ImageTk.PhotoImage(Work_Image_Prev) #Converts image object into format Tkinter can use
Image_Container = CanvasContainer.create_image(300,270, image = Work_Image) #Places image at said coordinates

#Image Location Text + Text Box
# Label(main_window, text="Image Location: ", background = BK_G_DEF, width=5, foreground = "White", font=("Helvetica", 14)).grid(row=IMAGE_ROW+15,column=WORK_COLUMN+1) #Creates label and places it on grid (save: highlightbackground="black", highlightthickness=1)
ImageLocation = Entry(main_window, width=32, borderwidth=2) #Creates input box
ImageLocation.grid(row=IMAGE_ROW+17, column=WORK_COLUMN, columnspan=2, sticky=S) #Places input box on grid

#Image output field
#Image_Location_Warning = Label(main_window, text="", background=BK_G_DEF, foreground="red") #Creates warning lable
#Image_Location_Warning.grid(row=10, column=WORK_COLUMN, columnspan=3) #Places it on grid

ImageOut = Text(main_window, width=67, height=22, borderwidth=2) #Creates textbox for output text 
ImageOut.grid(row=5, column=WORK_COLUMN+3, columnspan=3,rowspan=10) #Places it on grid
ImageOut.insert("end", f"Testing I have 8 words and 30 letters")

#!!!Functions
def ChangeImage():
    global PictureHolder
    
    #Verifying Input
    PreviewImageLocation=str(ImageLocation.get()) #Gets the value from user entered file path box4

    if( not path.isfile(PreviewImageLocation)): #If not a valid file path 
        print(f"This is a not path to a file{str(PreviewImageLocation)}") #Then display error message
        PreviewImageLocation = "" #Makes text field blank again since previous emtry was invalid
    else:
        pass

    '''
    else: #If it is a valid file path
        Image_Location_Warning.config(text=f"") #No warning text
    
    if(PreviewImageLocation == ""): #If not valid file path, say path not found and fill textbox with sample text
        Image_Location_Warning.config(text=f"path to '{ImageLocation.get()}' not found") #Warning pop up
        PreviewImageLocation = "./Train_data/text/sampletext.png" #Sample text
    '''

    ImageLocation.delete(0,END) #Clear text box
    ImageLocation.insert(0,PreviewImageLocation) #Insert sample text
    
    #Gathering data
    Work_Image_Prev = Image.open(PreviewImageLocation) #Opens user enetered file path
    (width, height) = (Work_Image_Prev.width, Work_Image_Prev.height) #Sets proper dimensions for opened image
    if(width > height):
        Ratio = 600/width
    else:
        Ratio = 510/height
    
    NewSize = (int(width*Ratio), int(height*Ratio)) #Stores dimensions in a variable
    PictureHolder = ImageTk.PhotoImage(Work_Image_Prev.resize(NewSize)) #Redimensions user opened image
    Work_Image_Prev.close() #Closes user entered file path
    CanvasContainer.itemconfig(Image_Container,image=PictureHolder) #Sets image

#Converts image to text and outputs result
def WordScanner():
    global SavedText
    PreviewImageLocation = str(ImageLocation.get()) #Gets the value from user entered file path box

    if( not path.isfile(PreviewImageLocation)): #If not a valid file path 
        print(f"This is a not path to a file{str(PreviewImageLocation)}") #Then display error message
        return #Terminates function

    TextFound = ImTeTs.getImageText(ImageLocation.get()) #Convert image to text and save it
    SavedText = TextFound
    ImageOut.delete(1.0,"end") #Clear text widget from beginning to end
    ImageOut.insert("end", f"{TextFound}") #Insert into text widget at the end (blank so front really)

#Accesses local directory, allows you to select file of any type and use it   
def browseFiles():
    filePath = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("PNG files", "*.png*"), ("all files", "*.*")))
    #Error if box has text already: Clear input box first
    ImageLocation.insert(tk.END, filePath) #Inserts selected file path in input box, need to click "Update Image" next 

#Text to speech
def Text2Speech():
    TextFound = ImageOut.get(1.0,"end-1c") #Retreives text from wordscanner output textbox
    if (len(TextFound) == 0): #If text is not found, display error 
        print(f"There is no text to read, please write in the text box or scan text from an image")
        return
    else: #Read the text found in textbox
        engine = pyttsx3.init() 
        engine.say(TextFound)
        engine.runAndWait()

#Saves scanned image text to 2 .txt files, a most recently scanned and a continuous history
def SaveIMG():
    #save to Scanned_History.txt
    ImTeTs.saveImageText(pathUsed=ImageLocation.get(), textGenerated=ImageOut.get("1.0",END))
    #save to TextStorage.txt
    ImTeTs.saveImageTextSingle(pathUsed=ImageLocation.get(), textGenerated=ImageOut.get("1.0", END))

def count_letters_and_words():
    sentence = ImageOut.get("1.0", "end-1c") #Get all text from start to end

    # Count letters
    letter_count = len(sentence.replace(" ", ""))

    # Count words
    word_count = len(sentence.split())

    WordOut.config(text=f"Word Count: {word_count}") #Update Label
    CharOut.config(text=f"Character Count: {letter_count}") #Update label

#Place holder
def Revert():
    global SavedText
    ImageOut.delete(1.0,"end")
    ImageOut.insert("end", f"{SavedText}")
    
#Performs languages conversion
def perform_translation():
        user_lang_input = LanguageOut.get() #Gets entered language choice

        if not user_lang_input.strip():
            print("Please select a language first.")
            return

        text_to_translate = ImageOut.get(1.0,"end-1c") #Gets text from read/entered text
        #print(user_lang_input)
        #print(text_to_translate)

        #Find the language that matches users input
        for name, code in languages:
            if user_lang_input.lower() in name.lower():
                print(f"Language chosen: {name} and {code}")
                break

        #If lnaguage entered matches
        if name:
                try:
                    translator = Translator(to_lang=code) #Setup translator to chosen language
                    translated_text = translator.translate(text_to_translate) #Convert text using new language
                    ImageOut.delete(1.0, "end") #Clear current text
                    ImageOut.insert("end", translated_text) #Insert translated text
                except Exception as e:
                    print("Translation failed: {e}")

        #If language entered doesnt match
        else:
                print("Language not found")

#Buttons/Labels/etc...
Label(main_window, text = "Welcome To Text Reader 9000", background = BK_G_DEF, foreground = "White", font=("Helvetica", 24)).grid(row=1, column=2, columnspan=3, rowspan=1)

Button(main_window, text="Update Image", command=ChangeImage, width=20, background=BUTTN_COLOR).grid(row=IMAGE_ROW+17,column=WORK_COLUMN-1, columnspan=2, rowspan=1, sticky=S)
Button(main_window, text="Browse Files", command=browseFiles, width=20, background=BUTTN_COLOR).grid(row=IMAGE_ROW+17,column=WORK_COLUMN+1, columnspan=2, rowspan=1, sticky=S)

Label(main_window, text="Image Analysis Output", background = BK_G_DEF, foreground = "White", font=("Helvetica", 20)).grid(row=3,column=4, columnspan=3, rowspan=2)

Button(main_window, text="Save Text", command=SaveIMG, background=BUTTN_COLOR).grid(row=IMAGE_ROW+14,column=WORK_COLUMN+3, sticky=E, padx = 15)
WordOut = Label(main_window, text="Word Count: 0", background = BK_G_DEF, foreground = "White", font=("Helvetica", 12))
WordOut.grid(row=15,column=5, columnspan=1, rowspan=1, sticky=W, padx=10)
CharOut = Label(main_window, text="Character Count: 0", background = BK_G_DEF, foreground = "White", font=("Helvetica", 12))
CharOut.grid(row=15,column=5, columnspan=2, rowspan=1)

Button(main_window, text="Word Scanner", command=WordScanner, background=BUTTN_COLOR, width=20).grid(row=16,column=4, columnspan=1, sticky=E)
Button(main_window, text="Count Words/Letters", command=count_letters_and_words, background=BUTTN_COLOR, width=20).grid(row=16,column=5, columnspan=1)
Button(main_window, text="Text to Speech", command=Text2Speech, background=BUTTN_COLOR, width=20).grid(row=16,column=6, columnspan=1, sticky=W)

LanguageOut = Entry(main_window, width=24, borderwidth=2) #Select Language Input Box
LanguageOut.grid(row=IMAGE_ROW+16, column=4, columnspan=2) #Places input box on grid
Button(main_window, text="Update Language", command=perform_translation, background=BUTTN_COLOR, width=20).grid(row=18,column=4, columnspan=2)
Button(main_window, text="Revert Language", command=Revert, background=BUTTN_COLOR, width=20).grid(row=19,column=4, columnspan=2)
lang_list = Listbox(main_window, height=6) # creates list box within new window
lang_list.grid(row=17, column=5, columnspan=2, rowspan=3, padx=0, pady=0) # places listbox on grid
# places every language within list box
for name, code in languages: 
    lang_list.insert(END, f"{name}")

#Run main window
main_window.mainloop()
