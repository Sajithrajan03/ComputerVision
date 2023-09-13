import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import pyautogui as auto
import time

cap = cv2.VideoCapture(0)

hd = HandDetector(maxHands=1, detectionCon=0.7)
while(1):
    rt,frame = cap.read()
    frame = cv2.resize(frame,(1080,720))
    hand,frame = hd.findHands(frame)
    cv2.imshow("frame",frame)
    cv2.waitKey(1)