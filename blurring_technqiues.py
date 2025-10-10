import cv2 as cv
import matplotlib.pyplot as plt

#blurring is used when there is a lot of noise caused by camera sensors, lighting etc.
#gaussian - most popular method
#kernel/window is a window drawn over an image
#the size is called the kernel size (rows and columns)
#a blur is applied to the middle pixel as a result of the surrounding pixels.
#the kernel slides to the right and then down to keep computing for all pixels in the image

img = cv.imread('Images/images.jpeg')
cv.imshow('Cat', img)

#BLURRING METHOD 1: AVERAGING
#define a kernel window
#it computes the pixel intensity of the middle pixel
# as the average of surrounding pixel intensities
#the bigger the kernel size, the bigger the blur
average=cv.blur(img,(3,3))
cv.imshow('Average Blur', average)


#BLURRING METHOD 2: GAUSSIAN BLUR
#instead of verage it gives a weight to each surround pixel
# and the average of the products of those weights gives the true center
# this will give less blurring than the averaging method, but has a more natural look
#the function takes in: the image, kernel size and
#   sigmax which is the standard deviation in the x direction
gauss = cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussian Blur', gauss)


#BLURRING METHOD 3: MEDIAN BLUR
#finds the median of the surrounding pixels
#generally, more effective at reducing noise than others
#good at reducing salt and pepper noise
#the function takes in the image, and kernel size - not a tuple but an int this time as opencv assumes it is a tuples
#not meant for high kernel sizes like 7 and sometimes even 5 - smduges image
median =cv.medianBlur(img,3)
cv.imshow('Median Blur', median)


#BLURRING METHOD 4: BILATERAL BLURRING
#most effective
#used in a lot of advanced CV projects
#traditional blurring methods, blur the image without looking at whether you're reducing the edges or not
#this method keeps edges
#the function takes in an image, diameter of pixel neighborhood(not the kernel size)
# sigma color- how many colors in the neighborhood will be considered
#   - higher = more colors considered
#sigma space - how many distant pixels will influence the blurring calculations
bilateral = cv.bilateralFilter(img,5,15,15)
cv.imshow('Bilateral Blur', bilateral)


cv.waitKey(0)