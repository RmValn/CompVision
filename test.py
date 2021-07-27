from math import sqrt
import cv2
import mediapipe as mp
import virtualvideo
import time
import HandTrackModule as htm
import numpy as np



def openHandDegree(lmList):
    pass
    # for i in lmList[0][2]-lmList[12][2]:
    #     print(i)

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)

def get_px_distance(p1,p2):
    xx = pow((lmList[p2][1]-lmList[p1][1]),2)
    yy = pow((lmList[p2][2]-lmList[p1][2]),2)
    dist = sqrt(abs(xx+yy))
    if dist == 0:
        return 1
    return dist

def get_cm_distance():
    return round(((90*513.2)/get_px_distance(5,17)/10),1)

detector = htm.handDetector()
while True:
    success, img = cap.read()
    img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    img = detector.findHands(img)
    img_gray = cv2.cvtColor(img,)
    lmList = detector.findPosition(img,draw=False)
    if len(lmList)!=0:    
        pass
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)),(0,40), cv2.FONT_HERSHEY_PLAIN,3,
                (255,0,0),3)


    cv2.imshow('Image',img)
    cv2.waitKey(1)