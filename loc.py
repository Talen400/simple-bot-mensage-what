import pyautogui
import time

while True:
    x, y = pyautogui.position() 
    print(f"Mouse Position: X = {x}, Y = {y}", end='\r') 
    time.sleep(0.1)