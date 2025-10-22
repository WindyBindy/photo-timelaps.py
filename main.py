# imports
import time

# constants
wholeTime = 1440
miniTime = 5
siances = 0


def photoFunc():
    print("photo")


# loop for wholeTime / miniTime
while wholeTime > miniTime:
    photoFunc()
    time.sleep(miniTime)
