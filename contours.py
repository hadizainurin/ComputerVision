import cv2 as cv

img = cv.imread('Photos/cats.jpg')

cv.imshow('Cats', img)

# Contours are basically the boundaries of object, the line or curve that joins the continous points along
# the boundary of an objects (Think of its like edge)
# From mathematical point of view, it is not edge
# Contours are useful tools for shape analysis, object detection and recognition