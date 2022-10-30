import cv2
import numpy as np

# Two postprocessing methods.=
def erosion(src):
    erosion_size = 15
    erosion_shape = cv2.MORPH_ELLIPSE
    element = cv2.getStructuringElement(erosion_shape, (2 * erosion_size + 1, 2 * erosion_size + 1), (erosion_size, erosion_size))
    erosion_dst = cv2.erode(src, element)
    return erosion_dst

def dilatation(src):
    dilatation_size = 15
    dilation_shape = cv2.MORPH_ELLIPSE
    element = cv2.getStructuringElement(dilation_shape, (2 * dilatation_size + 1, 2 * dilatation_size + 1),
                                       (dilatation_size, dilatation_size))
    dilatation_dst = cv2.dilate(src, element)
    return dilatation_dst


cam = cv2.VideoCapture(0)

while True:
    frameCaptured, frame = cam.read() #Load image from camera

    greyscale = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY) #Makes the image greyscale. This will hopefully help isolate the coins better, since it will be looking
                                                        # for shiny on a less vibrant background
    
    #highlight things in a certain boundary
    lb = np.array([128])
    ub = np.array([255])
    highlighetedImage = cv2.inRange(greyscale, lb, ub)
    
    postprocessedimage = dilatation(erosion(highlighetedImage))
    
    
    #Displaying the various images
    cv2.imshow("Window", frame)
    cv2.imshow("Greyscale", greyscale)
    cv2.imshow("Ranged Image", highlighetedImage)

    #If escape is pressed, end the loop, and therefore, the program
    if cv2.waitKey(10)==27:
        break
