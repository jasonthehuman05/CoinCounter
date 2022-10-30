import cv2
import numpy as np

# Two postprocessing methods.=
def erosion(src):
    erosion_size = 32
    erosion_shape = cv2.MORPH_ELLIPSE
    element = cv2.getStructuringElement(erosion_shape, (2 * erosion_size + 1, 2 * erosion_size + 1), (erosion_size, erosion_size))
    erosion_dst = cv2.erode(src, element)
    return erosion_dst

def dilatation(src):
    dilatation_size = 18
    dilation_shape = cv2.MORPH_ELLIPSE
    element = cv2.getStructuringElement(dilation_shape, (2 * dilatation_size + 1, 2 * dilatation_size + 1),
                                       (dilatation_size, dilatation_size))
    dilatation_dst = cv2.dilate(src, element)
    return dilatation_dst


cam = cv2.VideoCapture(0)
lbLim = 64
while True:
    frameCaptured, frame = cam.read() #Load image from camera

    greyscale = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY) #Makes the image greyscale. This will hopefully help isolate the coins better, since it will be looking
                                                        # for shiny on a less vibrant background
    
    #highlight things in a certain boundary
    lb = np.array([lbLim])
    ub = np.array([255])
    highlighetedImage = cv2.inRange(greyscale, lb, ub)
    
    #Does some postprocessing in an attempt to make blobs more accurate
    postprocessedImage = dilatation(erosion(highlighetedImage))
    
    #insert a bounding box around any detected blobs
    contours, hierarchies = cv2.findContours(postprocessedImage, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    blank = np.zeros(postprocessedImage.shape[:2], dtype='uint8')
    cv2.drawContours(frame, contours, -1, (255, 0, 0), 1)

    coinCount = len(contours)
    #Draw text to display current threshold
    cv2.putText(frame, f"CURRENT LOWER BOUND: {lbLim}", (0, 300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 2)
    cv2.putText(frame, f"COINS COUNTED: {coinCount}", (0, 350), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 2)

    #Displaying the various images
    cv2.imshow("Window", frame)
    #cv2.imshow("Greyscale", greyscale)
    #cv2.imshow("Ranged Image", highlighetedImage)
    #cv2.imshow("Postprocessed Image", postprocessedImage)

    
    key = cv2.waitKey(10)
    if key == 27: #If escape is pressed, end the loop, and therefore, the program
        break
    elif key == 61:
        lbLim += 1
    elif key == 45:
        lbLim -= 1

