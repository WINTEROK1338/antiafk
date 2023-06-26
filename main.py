import pyautogui
import pydirectinput
import time
import random
import mss
import numpy as np
from PIL import Image
import gc

def main():
    """
    Main function for the program
    """
    # Randomly will move right or left to keep from AFKing
    moveDirection = ["a", "d"]


    while True:

        # 20% chance to move to avoid AFK timer
        if random.randint(1, 3) == 3:
            key = moveDirection[random.randint(0, 1)]
            pyautogui.keyDown(key)
            time.sleep(.1)
            pyautogui.keyUp(key)
            time.sleep (60)


# Runs the main function
if __name__ == '__main__':
    main()
