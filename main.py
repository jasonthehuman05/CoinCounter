import cv2

cam = cv2.VideoCapture(0)

while True:
    frameCaptured, frame = cam.read() #Load image from camera

    greyscale = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    
    cv2.imshow("Window", frame) #Display image in window
    cv2.imshow("Greyscale", greyscale) #Display image in window
    if cv2.waitKey(10)==27:
        break
