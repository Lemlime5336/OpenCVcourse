import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
#note: histograms show the distribution of pixel intensities in an image
#      be it a color or greyscale image.
#      number of bins represent pixel intensities

img = cv.imread('Images/images.jpeg')
cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#GRAYSCALE HISTOGRAM
#images are a list so we need to pass in a list of images, in this case just 'gray'
# number of channels - the index of the channel we are computing the histogram for
#                      in this case grayscale, so a list of 0
#                      mask - histogram for a specific portion
#                      histSize - number of bins in the histogram
#                      ranges - range of all possible pixel values
gray_hist = cv.calcHist([gray],[0], None, [256],[0,256])
plt.figure()
plt.title('Grayscale histogram')
plt.xlabel('Bins')
plt.ylabel('Number of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

#HISTOGRAM WITH A MASK
blank = np.zeros(img.shape[:2], dtype='uint8')

circle=cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

mask = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow('Mask', mask)

gray_hist2 = cv.calcHist([gray],[0], mask, [256],[0,256])
plt.figure()
plt.title('Grayscale histogram')
plt.xlabel('Bins')
plt.ylabel('Number of pixels')
plt.plot(gray_hist2)
plt.xlim([0,256])
plt.show()




#COLOR HISTOGRAM
#the whole image
plt.figure()
plt.title('Color histogram')
plt.xlabel('Bins')
plt.ylabel('Number of pixels')
#define a tuple of colors
colors=('b','g','r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img],[i], None, [256],[0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.show()

#masked image
blank2 = np.zeros(img.shape[:2], dtype='uint8')
mask2=cv.circle(blank2, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
masked = cv.bitwise_and(img, img, mask=mask2)
cv.imshow('Masked image', masked)

plt.figure()
plt.title('Color histogram')
plt.xlabel('Bins')
plt.ylabel('Number of pixels')
#define a tuple of colors
colors=('b','g','r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img],[i], mask2, [256],[0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.show()


cv.waitKey(0)