import keyboard
import time

def start_hotkey_press():
    if keyboard.is_pressed("+"):
        print("Timer started.")

        time.sleep(0.1)

        return True

def end_hotkey_press():
    if keyboard.is_pressed("Enter"):
        return True