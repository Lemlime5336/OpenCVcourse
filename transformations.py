import cv2 as cv
import numpy as np

img = cv.imread('Images/images.jpeg')
cv.imshow('Cat', img)

#1. Translation
# shifting an image along x and y axis
#create a function which takes in an image and x and y coordinates
def translate(img, x,y):
    transMat= np.float32()

cv.waitKey(0)