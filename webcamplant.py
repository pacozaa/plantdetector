import covEX
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here    
    plantimg = covEX.convertGreenSerious(frame)
    # Display the resulting frame
    plantimg = cv2.flip(plantimg,1)
    cv2.imshow('frame',plantimg)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
