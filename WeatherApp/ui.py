import threading
import time
stop_animation = threading.Event()
stop_animation = threading.Event()

def animate():
    width = 30
    runner = "ᕕ( ᐛ )ᕗ"
    weather = "☁️"

    position = 0

    while not stop_animation.is_set():

        print(
            "\r" +
            " " * position +
            runner +
            "-" * (width - position) +
            weather,
            end="",
            flush=True
        )

        position += 1

        if position > width:
            position = 0

        time.sleep(0.08)

def start_animation():
    stop_animation.clear()
    animation_thread = threading.Thread(
        target= animate,
        daemon = True
    )
    animation_thread.start()
    return animation_thread

def stop():
    stop_animation.set()