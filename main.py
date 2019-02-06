import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    
    
    blured = cv2.blur(frame, (25,25))
    hsv = cv2.cvtColor(blured,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv,np.array([25,189,50]),np.array([95,255,198]))
    A = np.count_nonzero(mask)*256
    sumX = mask.sum(axis=0)
    mulX = np.multiply(sumX,np.arange(0,len(sumX)))
    comX = np.sum(mulX)/A
    print(np.sum(mulX),comX,len(mask[0]))
    cv2.imshow('Frame', mask)
    #print(frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
