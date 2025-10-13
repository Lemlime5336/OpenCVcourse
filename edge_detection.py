import cv2 as cv
import numpy as np

#gradients are edge-like regions in images
#they are not the same as edges

img = cv.imread('Images/images.jpeg')
cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#METHOD 1: LAPLACIAN
#this method takes in a source image, and a ddepth
#it computes the gradient of the grayscale image
lap=cv.Laplacian(gray, cv.CV_64F)
#when we transition from black to white and white to black,
#its considered a positive and negative slope
#images cannot have negative pixel values,
#so we compute the absolute value and convert to uint8 (image datatype)
lap=np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

#METHOD 2: SOBEL
#computes gradients in 2 directions, x and y
#it takes the image, ddpeth, x direction and y direction
#used most often in more advanced cases
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel=cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobelx', sobelx)
cv.imshow('Sobely', sobely)
cv.imshow('Combined Sobel', combined_sobel)

#METHOD 3: CANNY
#Canny is a multistage process and actually uses sobel in 1 stage
#much cleaner than the above
canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)


cv.waitKey(0)