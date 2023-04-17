from xmlrpc.client import Boolean
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con
import pymsgbox
import os


def click(x, y):
    pyautogui.moveTo(x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def checkImage(image):
    if pyautogui.locateOnScreen(image, confidence=0.8) != None:
        return True
    else:
        return False


def clickImage(image: str, timeSleep: float, plusY: float) -> Boolean:
    try:
        if pyautogui.locateOnScreen(image, confidence=0.8) != None:
            x, y = pyautogui.locateCenterOnScreen(image, confidence=0.8)
            click(x, y + plusY)
            time.sleep(timeSleep)
            return True
        return False
    except:
        return False

# function to start the program when press F1 key


prodArmy = "barbare"


def start():
    altTab = False
    startGame = False
    while True:
        if clickImage('elvenar/images/cross.png', 0.5, 0):
            continue
        elif clickImage('elvenar/images/piece.png', 0.1, 50):
            continue
        elif clickImage('elvenar/images/mat.png', 0.1, 50):
            continue
        elif clickImage('elvenar/images/zzz.png', 0.5, 50):
            prod = clickImage('elvenar/images/prod.png', 0.5, 0)
            if prod:
                altTab = True
        elif clickImage('elvenar/images/zzz2.png', 0.1, 50):
            prod = clickImage('elvenar/images/prod.png', 0.5, 0)
            if prod:
                altTab = True
        if altTab:
            keyboard.press_and_release('alt+tab')
            altTab = False
            time.sleep(1)


start()
