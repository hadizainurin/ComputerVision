# If you have problem importing OpenCV, then remember to ctrl+shift+p (VSC)
# change your Python interpreter to version 3.9
# For ML, used anaconda
import cv2 as cv

### Read a image from OpenCV
# img = cv.imread('Photos/cat_large.jpg') #Noted that OpenCV does not have an automatic way to deal with image larger than user computer screen
# # To allow us to use cat large, we have to resize its
# # Display the image as a new window
# cv.imshow('Cat', img) #name of the window, matrix of the image to display
# Keyboard waiting function
# cv.waitKey(0) #0 means its unlimited wait for keyboard to be pressed

### Read a video from OpenCV
# capture = cv.VideoCapture(0) #This will reference to your video capture device, 0 is the first camera, 1 is the second camera, so n is the n camera
capture = cv.VideoCapture('Videos/dog.mp4') #Reading a video

#This will read a video frame by frame
while True:
    isTrue, frame = capture.read() #This have two arg, its will return a frame and if not then the argument will be false
    cv.imshow('Video', frame)

    #If the letter d is pressed then break out of this loop
    if cv.waitKey(20) & 0xff==ord('d'): #Return a 32-bit integer corresponding to the pressed ley & bit mask which sets the left 24 bits to zero.
        break #End the while loop

capture.release()
cv.destroyAllWindows() #Clear all windows
# Noted: If you get -215:Assertion failed, then OpenCV can't find anymore frame after last frame, or its can no longer find the file associated with an image or video

### Resize and Rescaling OpenCV
# Method to change to resolution
# Only wWork for live video, not a standalone video file
def changeRes(width, height):
    capture.set(3,width) #The number is the properties of the capture class
    capture.set(4,height) #3 reference to width, and 4 reference to height
    # capture.set(10, brightness) #10 reference to brightness

# Method for AiO solution
def rescaleFrame(frame, scale=0.75):
    # Work for Images, Videos and live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimension = (width,height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)
