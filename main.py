import pyautogui
import time

time.sleep(5) #delay

f = open("text", "r")

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")