import cv2 as cv
import numpy as np

#there are 4 basic operators:
# and, or, xor, and not
#used a lot in image processing especially in masking
#pixels are turned off if it has a value of 0, on if 1

#basis to draw a ractangle and circle
blank = np.zeros((400,400), dtype="uint8")

#create a rectangle
# takes in a copy of the blank variable, starting point, ending point,
# color (as it is a binary image we can give one parameter), thickness
rectangle = cv.rectangle(blank.copy(), (30,30),(370,370),255,-1)

#create a circle
# takes in a copy of the blank variable, center, radius, color and thickness
circle=cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)


#BITWISE OPERATOR 1: AND
#returns the intersection - the common regions
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwise_and)

#BITWISE OPERATOR 2: OR
#returns the intersecting and non-intersecting regions
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)

#BITWISE OPERATOR 3: XOR
#returns the non-intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)

#BITWISE OPERATOR 4: NOT
#simply inverts the binary color
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('Bitwise NOT', bitwise_not)

bitwise_not2 = cv.bitwise_not(circle)
cv.imshow('Bitwise NOT2', bitwise_not2)

cv.waitKey(0)