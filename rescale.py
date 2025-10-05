'''
rescaling is modifying height and width
usually to a smaller value than original dimensions
'''
import cv2 as cv

#creating a function to rescale
#this method works for images, videos and live videos
#pass in the frame to be resized and scale value
def rescaleFrame(frame, scale=0.5):
    #as width and height are integers encode them from fp to int
    width=int(frame.shape[1]* scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    #resize() resizes the frame to a particular dimension
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

### Images (line 20-23)
img = cv.imread('Images/images.jpeg')
cv.imshow('Cat', img)
resized_image=rescaleFrame(img)
cv.imshow('Image',resized_image)

###read videos using open cv (line 26-37)
capture = cv.VideoCapture('Videos/IMG_1242.MOV')
while True:
    isTrue, frame = capture.read()

    #create a new frame
    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

#another way to resize videos
# is using the capture.set() method
#only works for live videos not images
#lines(46-50)
def changeRes(width,height):
    #3 and 4 are the properties of this capture clause
    #where 3 refers to width and 4 height
    capture.set(3, width)
    capture.set(4, height)


