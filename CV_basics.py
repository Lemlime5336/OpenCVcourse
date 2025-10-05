import cv2 as cv

img = cv.imread('Images/images.jpeg')
cv.imshow('Cat', img)

# #1. converting to grayscale
# # instead of colors we would only see the
# # intensity distribution of pixels
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)


# #2. Blurring image
# #reduces some noise in the image
# #this may be due to bad lighting, camera settings etc.
# #we pass the image and kernel size - kernel size has to be off
# blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# #to increase blurriness we increase the kernel size
# blur2 = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
#
# cv.imshow('Blur 2', blur2)


# # 3. Edge Cascade
# # helps find the edges in an image
# #pass in the image and 2 threshold values
# canny = cv.Canny(img, 125, 125)
# cv.imshow('Canny', canny)
#
# #we can reduce edges by blurring the image
# canny2 = cv.Canny(blur, 125, 125)
# cv.imshow('Canny 2', canny2)

# #4. dilating the image
# #dilating the image using a structural element
# #in this case the canny edges, with a kernel size and iterations
# dilated = cv.dilate(canny, (3,3), iterations=1)
# cv.imshow('Dilated', dilated)


# #5. eroding
# # we can erode the dilated image to get back
# # the structuring element
# # - we can get back almost the same edges as before
# eroded = cv.erode(dilated, (3,3), iterations=1)
# cv.imshow('Eroded', eroded)

# #6. resize
# #this ignores aspect ratio
# #by default there is an interpolation method in the background
# #called cv.INTER_AREA useful when shrinking images
# # when enlarging use INTER_LINEAR or INTER_CUBIC
# # cubic is slowest but resulting image is of better quality
# resize=cv.resize(img,(500,500))
# cv.imshow('Resized', resize)

# #7. cropping
# # images are arrays so we can use array slicing
# # to select portion of an image
# cropped = img[50:200, 200:400]
# cv.imshow('Cropped', cropped)

cv.waitKey(0)