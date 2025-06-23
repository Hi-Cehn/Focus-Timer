import datetime
import time

time_duration = 10

def setup(seconds):
    end = datetime.datetime.now() + datetime.timedelta(seconds=seconds)
    prev = datetime.datetime.now()

    return end, prev

def update(current, prev, time_duration):
    delta = current - prev

    if delta.total_seconds() >= 1:
        new_time = visual_update(time_duration)
        return current, new_time
    
    return prev, time_duration

def timer_visual(time_duration):
    mins, secs = divmod(time_duration, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end = "\r")

def visual_update(time_duration):
    time_duration -= 1
    timer_visual(time_duration)

    return time_duration
    


if __name__ == "__main__":
    end_time, prev = setup(time_duration)
    timer_visual(time_duration)

    while True:
        current = datetime.datetime.now()

        prev, time_duration = update(current, prev, time_duration)

        if end_time <= current:
            print("Time's up.")
            break

        time.sleep(0.01)
        