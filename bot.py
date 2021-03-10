import time
import pyautogui

time.sleep(5)  # This time allows the user to place the cursor
messages = open("message_collection.txt", "r")
for message in messages:
    pyautogui.typewrite(message)
    pyautogui.press("enter")