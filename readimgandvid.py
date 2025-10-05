###import libraries
import cv2 as cv

# ### read images using open CV (lines 5-12)
# #imread() take the path of an image and returns it as a matrix of pixels
# img = cv.imread('Images/images.jpeg')
#
# #imshow() displays the image using a new window
# cv.imshow('Cat', img)
#
#waits for a time in ms for a key to be pressed
# cv.waitKey(0)



###read videos using open cv (lines 17-46)
#capture variable is an instance of the VideoCapture clause
#VideoCapture() method takes integer arguments or path to video file
#integer arguments are for when a webcam or camera are connected to your computer
#webcam is usually 0
capture = cv.VideoCapture('Videos/IMG_1242.MOV')

#we use a while loop to read videos frame by frame
while True:
    #this part reads the video frame by frame
    #it returns the frame and a
    # boolean to say whether the frame was successfully read in or not
    isTrue, frame = capture.read()

    #to display an individual frame
    cv.imshow('Video', frame)

    #way to stop the video from playing indefinitely
    #0xFF==ord('d') means if the letter d is pressed
    #break out of the loop and stop playing the video
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

#now we can release the capture pointer
capture.release()
#and we can destroy all windows as we dont need them anymore
cv.destroyAllWindow()

#-215 Assertion failed error means open CV could not find a media file
#at the location you , it happened in this case
# because the video ran out of frames


