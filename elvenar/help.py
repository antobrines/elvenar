from xmlrpc.client import Boolean
from pyautogui import *
import pyautogui
import time
import win32api
import win32con


def click(x, y):
    pyautogui.moveTo(x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def checkImage(image):
    if pyautogui.locateOnScreen(image, confidence=0.8) != None:
        return True
    else:
        return False


def clickImage(image: str, timeSleep: float, plusY: float, confidence=0.8) -> Boolean:
    try:
        if pyautogui.locateOnScreen(image, confidence=confidence) != None:
            x, y = pyautogui.locateCenterOnScreen(image, confidence=confidence)
            click(x, y + plusY)
            time.sleep(timeSleep)
            return True
        return False
    except:
        return False

# function to start the program when press F1 key


def start():
    while True:
        if clickImage('elvenar/images/help-friend.png', 0.5, 0, 0.6):
            continue
        elif clickImage('elvenar/images/help-culture.png', 0.5, 0):
            continue
        elif clickImage('elvenar/images/help-hotel.png', 0.5, 0):
            continue
        elif clickImage('elvenar/images/help-reward.png', 0.5, 0, 0.6):
            continue
        elif clickImage('elvenar/images/help-ok.png', 0.1, 0):
            continue
        elif clickImage('elvenar/images/help-next.png', 0.1, 0):
            continue


start()
