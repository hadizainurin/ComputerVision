import numpy as np
import cv2 as cv
import os

haar_cascade = cv.CascadeClassifier('haar_face.xml') 

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
# features = np.load('features.npy', allow_pickle = True)
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

# def load_image_from_folder(folder):
#     images = []
#     for filename in os.listdir(folder):
#         img = cv.imread(os.path.join(folder,filename))
#         if img is not None:
#             images.append(img)
#         return images
#     return images 
# rootdir = "D:\Project\ComputerVision\Photos"
# for subdir, dirs, files in os.walk(rootdir):
#     for file in files:
#         img = cv.imread(os.path.join(subdir,file))

img = cv.imread(r'D:\Project\ComputerVision\Faces\train\elton john\2.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Person', gray)

# Detect the face in the image || Try Madonna and you see why this inbuilt face recogniser is not the best compare tu Azure Service
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+h]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0, 255, 0), thickness=2)

cv.imshow('Detected Face', img)
cv.waitKey(0)