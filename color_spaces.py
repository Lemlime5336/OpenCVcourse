import cv2 as cv
import matplotlib.pyplot as plt
#color spaces - system of representing an array of pixel colors like rgb, grayscale, hsv etc.

img = cv.imread('Images/images.jpeg')
cv.imshow('Cat', img)


#1. BGR to Grayscale
#this method takes in an image and the color code
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#2. BGR to HSV
#(hue saturation value - this is how humans think and see color)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#3. BGR to LAB (also represented as L*a*b)
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('Lab', lab)



#Note: open cv reads images in bgr format, but outside opencv, it is rgb,
#      so if we display the image using a python library (not opencv) colors will be inverted
plt.imshow(img)
plt.show()

#4. BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

#also visualize the rgb image in matplotlib
plt.imshow(rgb)
plt.show()



#Note: we can also do the inverse of the following:
#1. BGR to Grayscale
#2. BGR to HSV
#3. BGR to LAB (also represented as L*a*b)
#4. BGR to RGB
#But, grayscale cannot be directly converted to hsv, but we need to
# grayscale-->bgr-->hsv


#5. HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV to BGR', hsv_bgr)

#60, LAB to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB to BGR', lab_bgr)

cv.waitKey(0)