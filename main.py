import cv2
import aiming_static
import aiming_dynamic
import keyboard
import time
import config


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

        if mode == config.STATIC_MODE:
            aiming_static.run()

        elif mode == config.DYNAMEIC_MODE:
            aiming_dynamic.run()