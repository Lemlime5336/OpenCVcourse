'''
there are two ways we can draw
1. on a standalone image like th eone in img
2. or we can craete a dummy image

'''
import cv2 as cv
import numpy as np

#create a dummy image
#uint8 is the datatype of images
#pass width, height and number of color channels to shape
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

#1. paint the image a certain color
##reference all pixels
# blank[:] = 0,255, 0

#reference a range of pixels instead
# blank[200:300, 300:400]=0,0,255
# cv.imshow('Green', blank)

#2. draw a rectangle
#arguements include
# image to draw over;
# in this case pt 1 is the origin;
# and endpoint is 250,250
#color and thickness of the border
# thickness can be set to cv.FILLED or -1 to fill the rectangle
#cv.rectangle(blank, (0,0),(250,250),(0,255,0), thickness=2)

#alternative to fixed values of size:
#cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2), (0,255,0), thickness=-1)

#cv.imshow('Rectangle', blank)



#3. draw a circle
# cv.circle(blank, (250,250), 40,(0,0,255), thickness=3)
# cv.imshow('Circle', blank)



#4. draw a line
# cv.line(blank,(100,250),(300,400), (255,255,255), thickness=3)
# cv.imshow('Line', blank)



#5. write text on an image
# cv.putText(blank,'Hello', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=3)
# cv.imshow('Text', blank)
cv.waitKey(0)

