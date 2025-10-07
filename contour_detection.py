import cv2 as cv
import numpy as np

img = cv.imread('Images/images.jpeg')
cv.imshow('Cat', img)

#contours are boundaries of objects - not the same as edges
#contours are useful for shape analysis, object detection and recognition
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#we can draw the contours find by the thresholding method by creating a blank image
blank = np.zeros(img.shape, dtype="uint8")
cv.imshow('Blank', blank)

#EDGE DETECTION METHOD 1
blur=cv.GaussianBlur(gray,(3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#recommendation - use canny method first and find contours
canny=cv.Canny(blur, 125,175)
cv.imshow('Canny', canny)


# #to find contours we use the find contours method
# #this method returns 2 things: contours and hierarchies
# #takes in edges (canny) and a mode to find contours:
#     #cv.RETR_TREE for all the hierarchical contours
#     #cv.RETR_EXTERNAL for only external contours
#     #cv.RETR_LIST for all contours in the image
# #as well as the contour approximation method
#     #CHAIN_APPROX_NONE does nothing, simply returns all the contours
#     #CHAIN_APPROX_SIMPLE compresses all returned contours into a simpler one
# #it will look at the edges and return 2 values
# #1. the contours which would be a python list of all the contours
# #2. the hierarchies - the hierarchical representation of the contours
# contours, hierarchies = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
# #to get the number of contours:
# print(f'{len(contours)} contour(s) found')

##EDGE DETECTION METHOD 2
#the function takes the image, threshold value,maximum value, thresholding type
#threshold binarizes an image:
    #pixels<125 set to 0
    #pixels>125 set to 1
ret, thresh = cv.threshold(gray, 125,255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
#to get the number of contours:
print(f'{len(contours)} contour(s) found')

#takes image to draw over, the list of contours and
#contour index, we want all so set it to -1
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours drawn', blank)

cv.waitKey(0)