from time import sleep
import pyautogui

sleep(2) #sleep to click into where you want to paste
script = open('script.txt','r')
lines = script.readlines()

for line in lines: 
    #get rid of blank lines
    if not line.strip():
        continue
    pyautogui.typewrite(line.strip())
    pyautogui.press('enter')