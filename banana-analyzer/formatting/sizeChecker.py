import os
import cv2

"""
Checks images in all folder for minimum size (width) and (height)
"""

def belowMinSize(width, height):
    pathToImages = "../images"
    imageFolders = os.listdir("../images")
    count = 0

    for folder in imageFolders:
        folderPath = f"{pathToImages}/{folder}"
        images = os.listdir(folderPath)
        for image in images:
            imagePath = f"{folderPath}/{image}"
            imageData = cv2.imread(imagePath)
            if type(imageData) != type(None):
                w,h,c = imageData.shape
                if w < width or h < height:
                    print(imagePath)
                    count += 1

    print(f"There are {count} images under the size limit")
