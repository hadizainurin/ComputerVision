import cv2 as cv
import numpy as np

# This method show a drawable image
blank = np.zeros((500, 500, 3), dtype='uint8') # np.zeros --> generate an array containing zeros (imagine a 3x3  square fill with 0), color1, color2, shape of height
# cv.imshow('Blank', blank) #title, object
# This method show an image
# img = cv.imread('Photos/cat.jpg')
# cv.imshow('Cat', img)

# 1. Paint image a certain color
#blank[height_range1:width_range2]
# blank[200:300, 300:500] = 0,0,255 # 0,255,0 = Green, || 0,0, 255 = RED
# cv.imshow('Red', blank)

# # 2. Draw a Rectangle
# # Noted you can change (250,500) to (blank.shape[1]//2, blank.shape[0]//2)
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=cv.FILLED) #thickness=2 (line) || thickness=cv.Filled || thickness = -1
# cv.imshow('Rectangle', blank)

# # 3. Draw a Circle
# cv.circle(blank, (250,250), 40, (0,0,255), thickness = 3) #object, center, radius (pixel), color, thickness 
# cv.imshow('Circle', blank)

# # 4. Draw a standalone line
# cv.line(blank, (100,250), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness = 3) #img, starting pos, center, color, thickness 
# cv.imshow('line', blank)

# # 5. Write text on image
cv.putText(blank, 'Hello World', (0, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2) #image, text, original position, fontface
cv.imshow('Text', blank)

cv.waitKey(0)