import cv2
import static_aiming
import keyboard
import time
import config

static_mode = 1
dynamic_mode = 2

mode = int(input("Choose mode:\n " \
"1. static\n " \
"2. dynamic\n"))

auto_aim = False
start_time = None

while True:
    if keyboard.is_pressed('s'):
        auto_aim = True
        start_time = time.time()
    elif keyboard.is_pressed('e'):
        auto_aim = False

    if auto_aim:
        if (time.time() - start_time) * 1000 >= config.AUTO_AIM_DURATION:
            auto_aim = False

        if mode == static_mode:
            static_aiming.run()

        elif mode == dynamic_mode:
            mode = 0