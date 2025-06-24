def update(current, prev, time_duration):
    delta = current - prev

    if delta.total_seconds() >= 1:
        new_time = visual_update(time_duration)
        return current, new_time
    
    return prev, time_duration

def visual_update(time_duration):
    time_duration -= 1
    timer_visual(time_duration)

    return time_duration

def timer_visual(time_duration):
    mins, secs = divmod(time_duration, 60)
    print(f"{mins:02d}:{secs:02d}", end="\r")