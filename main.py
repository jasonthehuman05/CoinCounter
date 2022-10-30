import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while True:
    frameCaptured, frame = cam.read() #Load image from camera

    greyscale = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY) #Makes the image greyscale. This will hopefully help isolate the coins better, since it will be looking
                                                        # for shiny on a less vibrant background
    #highlight things in a certain boundary
    lb = np.array([128])
    ub = np.array([255])

    rangedimage = cv2.inRange(greyscale, lb, ub)
    
    cv2.imshow("Window", frame) #Display image in window
    cv2.imshow("Greyscale", greyscale) #Display image in window
    cv2.imshow("Ranged Image", rangedimage) #Display image in window
    if cv2.waitKey(10)==27:
        break
