from PIL import Image
from os import listdir, path
#conda install --channel conda-forge pillow
AcceptedImages = ['png', 'jpeg']

def GetAppFormated_Batch(PathUsed="", maxListSize=2):
    # createing starter items and verefying input
    if(not(path.exists(PathUsed))):
        print(f"This is an invalid path! \"{PathUsed}\"\n returning empty...")
        return []
    
    if(path.isfile(PathUsed)):
        print(f"This is a path to a file{PathUsed}\n using single form instead...")
        return Get_AppFormated_single(PathUsed=PathUsed)
    
    directoryItems = listdir(PathUsed)
    files = []
    
    for idx in range(len(directoryItems)):
        f = directoryItems[idx]
        if(idx >= maxListSize):
            break
        elif(f[len(f)-3:len(f)] in AcceptedImages):
            files.append(PathUsed+f)
        else:
            print(f"the folowing was in the path but not included: {f}")
    
    if (len(files) < 1):
        print(f"Path contains no valid items: {directoryItems}\n returning empty...")
        return []
    
    converted = []
    for f in files:
        converted.append(Get_AppFormated_single(PathUsed=f))
    
    print(f"\nfiles found: {files}")
    print(f"amount of images: {len(converted)}")
    image_sizes = []
    for i in converted:
        image_sizes.append(len(i))

    print(f"image sizes: {image_sizes}")
    print(f"out{converted[0]}")

    return converted

def Get_AppFormated_single(PathUsed="", maxListSize=2):
     # createing starter items and verefying input
    if(not(path.isfile(PathUsed))):
        print(f"This is not a valid path! \"{PathUsed}\"\n returning empty...")
        return []
    
    return GetAppFormated_Arr(file=PathUsed)


def GetAppFormated_Arr(file):
    #Generateing Data conversion
    img = Image.open(file)
    img.convert('RGB')

    Converted_Images = []

    imagew,imageH = img.size

    Converted_Image = [] # create new image object

    for w in range(imagew):
        for h in range(imageH):
            r, g, b, Alpha = img.getpixel((w,h))
            total = ((r + g + b)/3)/255

            Converted_Image.append(total) # push in pixel

    #Closing and returning dataset
    
    img.close()

    return Converted_Image

setpath = "Train_data\letters\TrainSet1\\"
GetAppFormated_Batch(PathUsed=setpath,maxListSize=8)
Get_AppFormated_single(PathUsed=setpath)