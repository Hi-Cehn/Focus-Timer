import keyboard
import time

def start_hotkey_press():
    if keyboard.is_pressed("+"):
        print("Key pressed.")

        time.sleep(0.1)

def end_hotkey_press():
    if keyboard.is_pressed("Enter"):
        return True