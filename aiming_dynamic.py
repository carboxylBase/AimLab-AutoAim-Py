import mss
import cv2
import numpy as np
import mouse_control
import vision
import config
import math

def run():
    closest1,closest2 = None,None
    with mss.mss() as sct:
        monitor = sct.monitors[1]     
        img = np.array(sct.grab(monitor))
        frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        mask = vision.preprocess(frame)
        mouse_pos = mouse_control.get_mouse_pos()
        targets, can_shoot = vision.find_targets(mask, mouse_pos)
        closest1 = vision.closest_to_mouse(targets, mouse_pos)

        if closest1 != (-1, -1) and can_shoot > 0:
            mouse_control.mouse_click()
            return

    with mss.mss() as sct:
        monitor = sct.monitors[1]     
        img = np.array(sct.grab(monitor))
        frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        mask = vision.preprocess(frame)
        mouse_pos = mouse_control.get_mouse_pos()
        targets, can_shoot = vision.find_targets(mask, mouse_pos)
        closest2 = vision.closest_to_mouse(targets, mouse_pos)

        k = 10

        if closest2 != (-1, -1):
            dx = closest2[0] - mouse_pos[0] + (closest2[0] - closest1[0]) * k
            dy = closest2[1] - mouse_pos[1] + (closest2[1] - closest1[1]) * k
            if can_shoot > 0:
                mouse_control.mouse_click()
            else:
                mouse_control.move_mouse_smooth(dx, dy)        