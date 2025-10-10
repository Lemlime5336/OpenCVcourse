import cv2 as cv
import numpy as np

img = cv.imread('Images/images.jpeg')
cv.imshow('Cat', img)

#color images consist of multiple color channels - red, green and blue
#all images are these three color channels merged together
#we can split an image into its respective color channels -
#split into blue, green and red components



#1. Splitting color channels
#b,g,r for each color channel --> blue, green and red
b,g,r = cv.split(img)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)



#2. merging color channels
merged = cv.merge([b,g,r])
cv.imshow('Merged', merged)

cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)




#3. look at actual color in the channel once split,
#by reconstructing the image
#blank image for reconstruction
blank = np.zeros(img.shape[:2], dtype='uint8')

blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])



cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)


cv.waitKey(0)