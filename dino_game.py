import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
hd = HandDetector(maxHands=1, detectionCon=0.7)

# Recoil detection variables
recoil_start_time = 0
recoil_duration = 0.5  # Adjust this duration as needed for your game

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (1080, 720))

    hands, frame = hd.findHands(frame)

    if hands:
        hand = hands[0]
        # Check if the index finger is pointing upwards
        if hand.fingers[1].isUp:
            #esdfsa
            # If the index finger is up, reset the recoil timer
            recoil_start_time = time.time()
        else:
            # If the index finger is down, check if the recoil duration has passed
            if time.time() - recoil_start_time > recoil_duration:
                # This indicates a recoil gesture, you can trigger the shooting action here
                print("Recoil Detected - Fire the Gun!")

    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
