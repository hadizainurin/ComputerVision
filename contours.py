from pickle import NONE
import cv2 as cv
from cv2 import THRESH_BINARY
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

# Draw a blank image, you can also specify image shape as (500, 500, 3), img.shape[:2]
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)
# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur) #This reduce the contours to 380
# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny Edges', canny)
## Instead of using blur and canny, we can also used threshold
### Why You can get away with contours and edges? Because we can look at canny and threshold methods that nearly yield at same result when show side by side

ret,thresh = cv.threshold(gray, 125, 255, THRESH_BINARY) #threshold look at image and trying to binaries that image, if threshold < 125 then its blank, if more then its white
cv.imshow('Thresh',thresh)
# findContours look at the structure of the image, look at the structuring elements
# or the edges of a found in the image and returns to values, the contours,
# which in Python is the list of all the coordinates of the contours that were
# hierachy is the representation that openCV trying to find inside the shape

contours, hierachies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) #image, mode(cv.RETR_), controur approximation method
print(f'{len(contours)} contour(s) found:!') #Look for how many contours is found, noted this is possible because contours is esentially a list

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

## Canny find contours use canny as the basic of detecting and finding the contours
# Approximation method none returns all of the contours || approx simple compressed all the contours that are returned into one simple that make most sense
# Noted you should blured the image before applying filter
# Why it make sense? because a line is defined by only two end points, which we don't have in approximate none method
## Noted regarding RETR
# RETR_EXTERNAL THE OUTSIDE OF CONTOUR || RETR_TREE RETURNED THE UNDERSCORE TREE

cv.waitKey(0)
# Contours are basically the boundaries of object, the line or curve that joins the continous points along
# the boundary of an objects (Think of its like edge)
# From mathematical point of view, it is not edge
# Contours are useful tools for shape analysis, object detection and recognition