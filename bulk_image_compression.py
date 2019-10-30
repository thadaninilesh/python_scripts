from PIL import Image
import os, sys

path = "/Users/nthadani/Desktop/screens/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            imageTemporary = Image.open(path+item)
            f, e = os.path.splitext(path+"resizedImages/"+item)
            newImage = imageTemporary
            print(f)
            print(item)
            newImage.save(f + '_newlyResized.jpg', 'PNG', quality=80)

resize()
