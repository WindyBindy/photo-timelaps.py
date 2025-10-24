# imports
import time
from cv2 import *

# constants
wholeTime = 20
miniTime = 5
siances = 0

timePased = miniTime * siances


def photoFunc():
    print("photo")


# loop for wholeTime / miniTime
while wholeTime > timePased:
    photoFunc()
    siances = siances + 1
    timePased = miniTime * siances
    print(timePased)
    time.sleep(miniTime)
