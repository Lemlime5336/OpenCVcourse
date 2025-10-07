import cv2 as cv
import numpy as np

img = cv.imread('Images/images.jpeg')
cv.imshow('Cat', img)

#1. Translation
# shifting an image along x and y axis
#create a function which takes in an image and x and y coordinates
def translate(img, x,y):
    #to translate an image we need to make a translation matrix
    #it takes a list with 2 lists inside of it, in the first
    transMat= np.float32([[1,0,x],[0,1,y]])
    #dimensions of the image which are a tuple of image width 1 and 0 height
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

#now we can translate.
# -x --> left
# -y --> up
# x --> right
# y -->down
translated = translate(img, 100,100)
cv.imshow('translated image', translated)




#2. rotation
#open cv allows to specify any point to rotate the image around
#create a function which takes an image, angle and rotation point
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    # we create a rotation matrix by passing the rotation point,
    # angle to rotate around and a scale value
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

#for clockwise rotation, positive values
#for anti-clockwise rotation, negative values
rotated=rotate(img, 45)
cv.imshow('rotated image', rotated)

#you can also rotate a rotated image
rotated_rotated = rotate(rotated, 45)
cv.imshow('rotated rotated image', rotated_rotated)


#3. Resizing
#shrinking --> INTER_AREA
#enlarging --> INTER_LINEAR or INTER_CUBIC (slower but resulting image is of better quality)
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('resized image', resized)

#4. Flipping
#flipcode of 0 --> vertical flip
#flipcode of 1 --> horizontal flip
#flipcode of -1 --> flipping both vertically and horizontally
flip = cv.flip(img, 0)
cv.imshow('flipped image', flip)

#5. cropping
cropped = img[200:400, 300:400]
cv.imshow('cropped image', cropped)

cv.waitKey(0)