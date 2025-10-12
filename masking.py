import cv2 as cv
import numpy as np

#using bitwise operations we can do masking
# allows to focus on certain parts of an image

img = cv.imread('Images/images.jpeg')
cv.imshow('Cat', img)

#dimensions of the mask have to be the same size as the image
#or it will fail and throw an error
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

#a circle will be the mask
#drawn on the blank image, center, radius, color and thickness
mask = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', mask)


#to create a masked image pass:
# source image, and parameter (in this case the mask)
masked_img = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked Image', masked_img)

# weirdly shaped mask
rectangle = cv.rectangle(blank.copy(), (30,30),(370,370),255,-1)
weird_shape=cv.bitwise_and(mask, rectangle)
cv.imshow('Weird Shape', weird_shape)

masked_img2 = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow('Masked Image 2', masked_img2)



cv.waitKey(0)