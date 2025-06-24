import datetime
import time

import timer
import shortcuts

time_duration = 10

def setup(seconds):
    end = datetime.datetime.now() + datetime.timedelta(seconds=seconds)
    prev = datetime.datetime.now()

    return end, prev

def start(time_duration):
    end_time, prev = setup(time_duration)
    timer.timer_visual(time_duration)

    return end_time, prev

if __name__ == "__main__":
    while not shortcuts.start_hotkey_press():
        time.sleep(0.01)
        pass
    
    end_time, prev = start(time_duration)

    while True:
        current = datetime.datetime.now()

        prev, time_duration = timer.update(current, prev, time_duration)

        if end_time <= current:
            print("Time's up.")
            break

        time.sleep(0.01)