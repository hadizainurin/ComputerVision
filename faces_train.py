### TRAINING THE SAMPLES IMAGES
## Also shows how to append list

from importlib.resources import path
import os
from pathlib import Path
import cv2 as cv
import sys
import numpy as np

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

## Debugging
#cwd = os.getcwd() #get the current directory
#print(cwd) # This is opposed to the idea of using absolute path and just used the current directory as a reference

DIR = Path("Faces/train/") # Path for train list
print(DIR.parent.absolute())

# Detect the face in the image, use haar cascadde verifier (Noted this is sensitive to noise)
haar_cascade = cv.CascadeClassifier('haar_face.xml') #Used haar face classifier

## Test logic for appending list
# p = []
# #for i in os.listdir(r'Faces\train'): # Noted do its either as raw string literals  r ' ' or 'C:\\Direcxtory\\File
# for i in os.listdir(path):
#     p.append(i)
# print(p) # check for the list

features = []
labels = []

def create_train(): # Train the modules
    for person in people: # This will loop in the folder and the people are the celebrity
        path = os.path.join(DIR, person)
        print("IS THIS THE CORRECT PATH?", path) # Debugging
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            # Read the image from this path
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            
            # Label to numerical values is to reduce the strain of computer memory by mapping
            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label) #Turn label to numeric

create_train()
print('TRAINING 100% COMPLETED ----------------------')

# Convert to numpy array

features = np.array(features, dtype = 'object')
labels = np.array(labels)

# ## Debugging 
# print(f'Length of the features = {len(features)}')
# print(f'Length of the labels = {len(labels)}')

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the face recogniser module on the feature list and the labels list
face_recognizer.train(features,labels)
face_recognizer.save('face_trained.yml') # Save the face recogniser so we don't have to repeat the process again
np.save('features.npy', features)
np.save('labels.npy', labels)

