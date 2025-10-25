# imports
import time
import cv2
import pygame
import datetime

wholeTimeInHours = 24
miniTimeInMinutes = 3


# constants
wholeTime = wholeTimeInHours * 60 * 60
miniTime = miniTimeInMinutes * 60
siances = 0

timePased = miniTime * siances
nameOfTheFile = "1.jpg"
width = 1280
height = 720
# Initialize pygame window (optional if just saving image)
pygame.init()
# Open camera


# frame is in BGR -> Convert to RGB (correct colors)
# frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


def photoFunc():
    cap = cv2.VideoCapture(2)  # 0 = first camera
    if not cap.isOpened():
        print("error")
        exit()
    cap.set(3, width)
    cap.set(4, height)
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
    # Warm up camera (discard first frames)
    for i in range(5):
        ret, frame = cap.read()
    # Save normal image

    cv2.imwrite(f"./images/{siances}.jpg", frame)
    cap.release()


# loop for wholeTime / miniTime
while wholeTime > timePased:
    siances = siances + 1
    timePased = miniTime * siances
    photoFunc()
    print(timePased)

    print("estimate time in hours:", wholeTimeInHours - timePased / 60 / 60)
    time.sleep(miniTime)
