read and show video stream , capture image
detect face and show bounding box(haarcascade)
flatten the largest face image and save in numpy array
repeat the above for multiple people to generate training data

import cv2
import numpy

#init camera
cap=cv2.VideoCapture(0)

#face dtection
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

while True:
    ret,frame =cap.read()

    if ret==False:
        continue

    cv2.imshow("Frame",frame)

    key_pressed=cv2.waitKey(1) & 0xFF
    if key_pressed == ord("q"):
        break
