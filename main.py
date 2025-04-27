import cv2
import aiming_static
# import aiming_dynamic
import keyboard
import time
import config
import win32gui
import sys

mode = config.STATIC_MODE
print("Push 'S' to start.")
# mode = int(input("Choose mode:\n " \
# "1. static\n " \
# "2. dynamic\n"))

auto_aim = False
start_time = None

WINDOW_TITLE = "aimlab_tb"
global aimlab_tb_hwnd
aimlab_tb_hwnd = win32gui.FindWindow(None, WINDOW_TITLE)
if aimlab_tb_hwnd == 0:
    print("No window found")
    sys.exit(0)

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
            aiming_static.run(aimlab_tb_hwnd)

        # elif mode == config.DYNAMEIC_MODE:
            # aiming_dynamic.run()