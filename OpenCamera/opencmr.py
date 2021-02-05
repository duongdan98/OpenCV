import cv2
import numpy as np 
cam=cv2.VideoCapture(0)
if not cam.isOpened():
    print("khong mo duoc camera")
while True:
    ret,frame=cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()