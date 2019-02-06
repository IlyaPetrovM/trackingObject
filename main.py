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
    
    sumY = mask.sum(axis=1)
    mulY = np.multiply(sumY,np.arange(0, len(sumY)))
    comY = np.sum(mulY)/A
    if comY > 0:
        pass
    else:
        comY = 0
    if comX > 0:
        pass
    else:
        comX = 0
    
    #print(comX,comY)
    #incolor = cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
    cv2.circle(frame, (int(comX),int(comY)),5, [0,0,255],5)
    cv2.imshow('Frame', frame)
    #print(frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
