import datetime
import time

def setup(seconds):
    end = datetime.datetime.now() + datetime.timedelta(seconds=seconds)

    return end


if __name__ == "__main__":
    end_time = setup(10)

    while True:
        current = datetime.datetime.now()

        if end_time <= current:
            print("Time's up.")
            break

        time.sleep(0.01)
        