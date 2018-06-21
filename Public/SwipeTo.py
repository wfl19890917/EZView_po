'''
Created on 2018年6月21日

@author: admin
'''
from appium import webdriver
from time import sleep 
from appium.webdriver.common.touch_action import TouchAction
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
def swipeUp(driver, t=500, n=1):
    l = driver.get_window_size()
    x1 = l['width'] * 0.5  # x閸ф劖鐖�
    y1 = l['height'] * 0.75  # 鐠у嘲顫恲閸ф劖鐖�   # 缂佸牏鍋閸ф劖鐖�
    y2 = l['height'] * 0.125 
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)

def swipeDown(driver, t=500, n=1):
    l = driver.get_window_size()
    x1 = l['width'] * 0.5  # x閸ф劖鐖�
    y1 = l['height'] * 0.25  # 鐠у嘲顫恲閸ф劖鐖�
    y2 = l['height'] * 0.75  # 缂佸牏鍋閸ф劖鐖�
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)

def swipLeft(driver, t=500, n=1):
    l = driver.get_window_size()
    x1 = l['width'] * 0.75
    y1 = l['height'] * 0.5
    x2 = l['width'] * 0.25
    y2 = l['height'] * 0.5
    for i in range(n):
        driver.swipe(x1, y1, x2, y2, t)

def swipRight(driver, t=500, n=1):
    l = driver.get_window_size()
    x1 = l['width'] * 0.25
    y1 = l['height'] * 0.5
    x2 = l['width'] * 0.75
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)

