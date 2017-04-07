import covEX
import numpy as np
import cv2

cap = cv2.VideoCapture(1)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    plantimg = covEX.convertGreenPlant(frame)
    residueimg = covEX.convertRed(frame)
    # Display the resulting frame
    plantimg = cv2.flip(plantimg,1)
    residueimg = cv2.flip(residueimg,1)
    frame = cv2.flip(frame,1)
    cv2.imshow('frame-colour',frame)
    cv2.imshow('frame-plant',plantimg)
    cv2.imshow('frame-red',residueimg)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
