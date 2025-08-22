import pyautogui
import time

pyautogui.FAILSAFE = True

pyautogui.position()
time.sleep(1)
print(pyautogui.position())
