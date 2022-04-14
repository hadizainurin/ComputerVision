import cv2 as cv

img = cv.imread('photos/park.jpg')
cv.imshow('Cat', img)

# Converting to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Blur an image
# Blur image remove some noise from the image due to camera sensors, bad lightning, etc.
# Gausassian Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT) #img, kernnal size short ksize (OddNumber)
cv.imshow('Blur', blur)

# Edge Cascade
# Finding the edge that is presence in the image
# Canny edge detector, a multistep process that involve blurring, grading, and so on
# You can reduce the edges by using the blur image instead of the color image
# The more blur you have, the less edge will produced
canny = cv.Canny(blur, 125, 175) #img,threshold1, threshold2 || Change img --> blur
cv.imshow('Canny Edges', canny)

# Dilating the image of the cascade image that is found
# Basically make the line more thicker
dilated = cv.dilate(canny, (7,7), iterations=3) #Dilation can be applied more than =1
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (3,3), iterations=3)
cv.imshow('Eroded', eroded)

# Resize an image
resize = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC) #Resize ignoring the aspect ratio
#Interpolation is useful if you are resizing smaller than dimension of orignial image
cv.imshow('Resized', resize)

# Cropping
cropped = img[50:200, 200:400] # Used array slicing for cropping
cv.imshow('Cropped', cropped)


cv.waitKey(0)