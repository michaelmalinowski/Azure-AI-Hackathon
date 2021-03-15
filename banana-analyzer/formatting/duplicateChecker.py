import os
import cv2

"""
Checks images in all folder for minimum size (width) and (height)
"""

def checkForDups():
    pathToImages = "../images"
    imageFolders = os.listdir("../images")

    imagesList = {}

    for folder in imageFolders:
        folderPath = f"{pathToImages}/{folder}"
        images = os.listdir(folderPath)
        for image in images:
            imagePath = f"{folderPath}/{image}"
            imageSize = os.path.getsize(imagePath)
            try:
                imageName = imagesList[str(imageSize)]

                print(f"{imagePath} is the same as {imageName}")
            except:
                imagesList[str(imageSize)] = imagePath

    
            
            
            


def belowMinSize(width, height):
    pathToImages = "../images"
    imageFolders = os.listdir("../images")

    for folder in imageFolders:
        folderPath = f"{pathToImages}/{folder}"
        images = os.listdir(folderPath)
        for image in images:
            imagePath = f"{folderPath}/{image}"
            imageData = cv2.imread(imagePath)
        
            w,h,c = imageData.shape
            if w < width or h < height:
                print(imagePath)
                count += 1