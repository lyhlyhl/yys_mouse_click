import pyautogui
import win32api
import win32con
import win32gui
import time
import random


def getPhotoPositon(png):   #利用pyautogui的函数得到x, y轴位置
    location = pyautogui.locateOnScreen(png)
    lefttop = (location.left, location.top)
    righttop = (location.left+location.width, location.top)
    leftdown = (location.left, location.top+location.hight)
    rightdown = (location.left+location.width, location.top+location.hight)
    return lefttop, righttop, leftdown, rightdown

def MouseMove(x, y):  # 移动鼠标的位置
    win32api.SetCursorPos((x, y))


def MouseClick(x=None, y=None):  # 鼠标点击指定的地方
    if not x is None and not y is None:
        MouseMove(x, y)
        time.sleep(0.005)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(random.uniform(0.001, 0.02))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

getPhotoPositon("./img/necessary/notchallenge.png")