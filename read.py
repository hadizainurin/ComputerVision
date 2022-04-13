# If you have problem importing OpenCV, then remember to ctrl+shift+p
# change your Python interpreter to version 3.9
# For machine learning, used anaconda
import cv2 as cv

# Read a image from OpenCV
img = cv.imread('Photos/cat.jpg')
# Display the image as a new window
cv.imshow('Cat', img) #name of the window, matrix of the image to display
# Keyboard waiting function
cv.waitKey(0) #0 means its unlimited wait for keyboard to be pressed

