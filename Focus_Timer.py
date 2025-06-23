import time

import keyboard

while True:
    if keyboard.is_pressed("+"):

        print("Key pressed.")

        time.sleep(0.1)

    if keyboard.is_pressed("Enter"):
        break

    time.sleep(0.01)

