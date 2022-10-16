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
    pymsgbox.alert(
        'Press "j" to start \nPress "k" to exit \nPress "," to pause it', 'Elvenar Bot')
    while True:
        if keyboard.is_pressed('j'):
            response = pymsgbox.confirm(
                'Are you sure you want to start the bot?', 'Elvenar Bot')
            if response == 'OK':
                startGame = True
            else:
                startGame = False
        if keyboard.is_pressed('k'):
            response = pymsgbox.confirm(
                'Are you sure you want to exit the bot?', 'Elvenar Bot')
            if response == 'OK':
                os._exit(1)
        elif startGame:
            if keyboard.is_pressed('k'):
                response = pymsgbox.confirm(
                    'Are you sure you want to exit the bot?', 'Elvenar Bot')
                if response == 'OK':
                    os._exit(1)
            if keyboard.is_pressed(','):
                response = pymsgbox.confirm(
                    'Are you sure you want to pause the bot?', 'Elvenar Bot')
                if response == 'OK':
                    startGame = False
            if clickImage('images/help-friend.png', 0.5, 0):
                time.sleep(0.2)
                clickImage('images/help-culture.png', 0.5, 0)
                clickImage('images/help-hotel.png', 0.5, 0)
                time.sleep(0.2)
            elif clickImage('images/help-reward.png', 0.1, 0):
                time.sleep(0.3)
                continue
            elif clickImage('images/help-ok.png', 0.1, 0):
                time.sleep(0.3)
                continue
            elif clickImage('images/help-next.png', 0.1, 0):
                time.sleep(0.3)
                continue


start()
