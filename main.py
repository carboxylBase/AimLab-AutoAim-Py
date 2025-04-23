import cv2
import numpy as np
import time
import mss
import sys
import os
sys.path.append(os.path.dirname(__file__))
import static_aiming.mouse_control
import static_aiming.vision
import static_aiming.config

static_mode = 1
dynamic_mode = 2

mode = input("Choose mode:\n " \
"1. static\n " \
"2. dynamic\n")

auto_aim = False
start_time = None

cv2.namedWindow("Screen", cv2.WINDOW_KEEPRATIO)
cv2.namedWindow("Mask", cv2.WINDOW_KEEPRATIO)

if mode == static_mode:
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        while True:
            key = cv2.waitKey(1)
            if key == ord('s'):
                auto_aim = True
                time.sleep(3)
                start_time = time.time()
            elif key == ord('e'):
                auto_aim = False

            if auto_aim:
                if (time.time() - start_time) * 1000 >= static_aiming.config.AUTO_AIM_DURATION:
                    auto_aim = False

                img = np.array(sct.grab(monitor))
                frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
                mask = static_aiming.vision.preprocess(frame)
                mouse_pos = static_aiming.mouse_control.get_mouse_pos()
                targets, can_shoot = static_aiming.vision.find_targets(mask, mouse_pos)
                closest = static_aiming.vision.closest_to_mouse(targets, mouse_pos)
                if closest != (-1, -1):
                    dx = closest[0] - mouse_pos[0]
                    dy = closest[1] - mouse_pos[1]
                if can_shoot > 0:
                    static_aiming.mouse_control.mouse_click()
                else:
                    static_aiming.mouse_control.move_mouse_smooth(dx, dy)

elif mode == dynamic_mode:
    mode = 0


cv2.destroyAllWindows()