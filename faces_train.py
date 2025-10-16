#use opencv's built in face  recognizer and train on all imaged in faces/train folder
import os
import cv2 as cv
import numpy as np

#1. create a list of all the people in the images
#method 1 to create a list
people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Mindy Kaling', 'Madonna']

#method 2
p = []
for i in os.listdir('Faces/train'):
    p.append(i)
print(p)

#2. create a variable called dir and set it to the base folder
DIR = r'Faces/train'

haar_cascade = cv.CascadeClassifier('haar_face.xml')


#3. create a function that loops over every folder in the base folder,
#and loop over every face in that image and add it to the training set

#our training set consists of 2 lists:
#1. features - image arrays of faces
#2. labels - corresponding labels
features = []
labels = []

def create_train():
    #loop over every person in the people list
    for person in people:
        #grab the path for the person
        path = os.path.join(DIR, person)
        label = people.index(person)

        #loop over every image in the folder
        for img in os.listdir(path):
            #grab the image path, and join the path to the image
            img_path = os.path.join(path, img)

            #read an image from the path
            img_array = cv.imread(img_path)
            #convert to grayscale
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                #retrieve faces region of interest
                faces_roi = gray[y:y+h,x:x+w]
                #append to the features list and append the corresponding labels to the labels list
                features.append(faces_roi)
                #the label variable is the index of the people list
                #this creates a map between the string label to an integer to reduce computational load
                labels.append(label)

create_train()
print(f'Length of features = {len(features)}')
print(f'Length of labels = {len(labels)}')
print('Training done')


#before training we need to convert features and labels to numpy arrays
features = np.array(features, dtype='object')
labels = np.array(labels)

#4. we can use the features and labels list now that it is appended to train a recognizer
#we instantiate the face recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()

#train the recognizer on feature list and labels list
face_recognizer.train(features,labels)

np.save('features.npy', features)
np.save('labels.npy', labels)

#note:
# if we intend to use this face recognizer in another file,
# we will have to repeat the whole process, instead opencv allows to save the trained model to use it by using the YAML source file
face_recognizer.save('face_trained.yml')