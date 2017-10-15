import cv2
import numpy as np

cam=cv2.VideoCapture(0)
kermel=np.ones((5,5),np.uint8)
while (True):
    _,frame=cam.read()
    rango_max=np.array([255,50,50])
    rango_min=np.array([0,0,0])
    mascara=cv2.inRange(frame,rango_min,rango_max)
    opening=cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kermel)

    x,y,w,h=cv2.boundingRect(opening)
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)
    #contours, _ = cv2.findContours(opening, 1, 2)
    _, contours, hierarchy = cv2.findContours(opening, 1, 2)
    #_, contours, hierarchy = cv2.findContours(thresh1.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    for i in range(len(contours)):
        cnt=contours[i]
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(frame,(x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('cámara',frame)
    cv2.imshow('color',opening)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
