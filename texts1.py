from time import sleep
from pynput.keyboard import Key, Controller

sleep(2)
script = open('script.txt','r')
lines = script.readlines()
keyboard = Controller()

for line in lines: 
    if not line.strip():
        continue

    for char in line.strip():
        keyboard.press(char)
        keyboard.release(char) 
        
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(0.2) #Change time for sending speed