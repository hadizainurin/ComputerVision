import cv2 as cv
import numpy as np

img = cv.imread('photos/park.jpg')

cv.imshow('Boston', img)

# Translatio means shifting an image along the x and y axis.
def translate (img, x, y):
    # Create a translation Matrix
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

## Values shift
# -x --> Left
# x --> Right
# -y --> Up
# y --> Down

translated = translate(img, -100, 100)
cv.imshow('Translated',translated)

# Rotation
# rotating an image by an angle
# OpenCV allows user to specify the point that user want to rotate the image
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    # Assumed that we want to rotate at the center
    if rotPoint is None:
        rotPoint = (width//2, height // 2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) #rotpoint, angle, scale value
    dimension = (width,height)

    return cv.warpAffine(img, rotMat, dimension)

rotated = rotate(img, 45) #negative value --> clockwise, positive value --> anti-clockwise
#Noted: You can also rotated the rotate image
# So make another rotation object
cv.imshow('Rotated', rotated)

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC) #INTER_AREA is default interpolation
cv.imshow('Resized', resized)

# Flipping
# 0 flip the image vertically (x-axis) || 1 flip the image horizantally (y-axis) || -1 flip the image both way 
flip = cv.flip(img, 1) #range of flip 0,1, or -1 
cv.imshow('Flip', flip)

# Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)