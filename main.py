import datetime
import time

import timer
import shortcuts

focus_duration = 5
relax_duration = 900

def setup(seconds):
    end = datetime.datetime.now() + datetime.timedelta(seconds=seconds)
    prev = datetime.datetime.now()

    return end, prev

def start(time_duration):
    end_time, prev = setup(time_duration)
    visual = timer.timer_visual(time_duration)
    print(visual, end="\r")

    return end_time, prev

def focus_loop(focus_duration):
    end_time, prev = start(focus_duration)

    while True:
        current = datetime.datetime.now()

        prev, focus_duration = timer.update(current, prev, focus_duration)

        if end_time <= current:
            print("Time's up.")
            break

        time.sleep(0.01)

if __name__ == "__main__":
    while not shortcuts.start_hotkey_press():
        time.sleep(0.01)
        pass

    focus_loop(focus_duration)

    end_time, prev = start(relax_duration)

    while True:
        current = datetime.datetime.now()

        prev, relax_duration = timer.update(current, prev, relax_duration)

        if end_time <= current:
            print("Time's up.")
            break

        time.sleep(0.01)