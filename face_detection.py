import cv2 as cv
#detecting faces in opencv using Haarcascade
#face detection is performed using classifiers.
#classifiers are algorithms which decide whether a given image is positive or negative
#classifiers are typically trained on thousands of images, opencv comes with pre-trained classifiers
#the 2 main ones are:
#1. Haarcascades
#2. Local Binary Patterns (advanced Haarcascades, not as prone to noise)

#for videos detect haarcascades for each individual frame of the video

import cv2 as cv

img = cv.imread('Images/woman.jpg')
cv.imshow('Woman', img)

#face detection does not involve skin tone or color
#haarcascade looks at an object in an image and
#based on edges tries to determine whether it is a face or not
#so we don't need color
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray lady', gray)

#reading the haar_face xml file
haar_cascade = cv.CascadeClassifier('haar_face.xml')

#the method takes in the image, scale factor,
#minimum neighbors - specifies the number of neighbors a rectangle
#                    needs to have to be considered a face
#detectMultiScale is an instance of the Cascade Classifier class which takes
#the image, uses the variables passed to detect a face and
#return the rectangular coordinates of that face as a list to faces_rect
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(f'Number of faces found = {len(faces_rect)}')

#since faces_rect are the coordinates we can loop over the list
#and draw a rectangle over the detected faces
for (x,y,w,h) in faces_rect:
    #draw a rectangle over the original image, pass point one, point 2,
    # color (green in this case) and a thickness
    cv.rectangle(img, (x,y),(x+w, y+h), (0,255,0), thickness=2)
cv.imshow('Detected faces', img)



#try with an image of a group of people
#haarcascade is very sensitive to noise
#makes errors, this is partially owing to noise
#increase min_neighbors or change scale factor to reduce sensitivity to noise
img = cv.imread('Images/group.jpg')
cv.imshow('Group', img)

gray2 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Group', gray2)
faces_rect2 = haar_cascade.detectMultiScale(gray2, scaleFactor=1.1, minNeighbors=3)
print(f'Number of faces found = {len(faces_rect2)}')
for (x,y,w,h) in faces_rect2:
    #draw a rectangle over the original image, pass point one, point 2,
    # color (green in this case) and a thickness
    cv.rectangle(img, (x,y),(x+w, y+h), (0,255,0), thickness=2)
cv.imshow('Detected faces', img)

#makes errors, this is partially owing to noise
#increase min_neighbors or change scale factor to reduce sensitivity to noise
#not the most effective at detecting faces, though popular
#not for more advanced Cv projects,
#Dlib Frontal Face Detector (HOG + Linear SVM) is better

cv.waitKey(0)