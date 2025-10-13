import cv2 as cv

#Thresholding is a binarization of an image
# convert it into pixels of 0 (black) or 255 (white)
# each pixel in an image is compared with a "threshold value"
# if the pixel intensity is less than threshold value, the value is set to 0
# else set to 255


img = cv.imread('Images/images.jpeg')
cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# 1. Simple Thresholding
# we use cv.threshold function which returns threshold (the threshold value we pass in)
# and thresh (the binarized image)
# we need to pass in the image, threshold value,
# maximum value (if the pixel value is greater than thresh what it will be changed to)
# and thresholding type - this looks at all pixels in the image
#                         and compares with threshold value.
#                         in this case t>150 = 255 and t<150 = 0
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholding', thresh)

#we can also create an inverse thresholded image
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholding Inversed', thresh_inv)





#2. Adaptive Thresholding
# Note: useful when dealing with multiple images, different images
#       have different threshold values, so having the computer find
#       the optimal threshold value would be ideal.
#this method takes in the image, maxvalue, adaptive thresholding method, thresholding type,
#block size - kernel size to compute the optimal threshold value,
#c value - an integer subtracted from the mean, to fine tune thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11,3)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

# another method is gaussian
adaptive_thresh_g = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11,3)
cv.imshow('Adaptive Thresholding - Gaussian', adaptive_thresh_g)

cv.waitKey(0)