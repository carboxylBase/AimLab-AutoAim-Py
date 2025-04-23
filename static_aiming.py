import mouse_control
import vision
import mss
import cv2
import numpy as np

def run():
    with mss.mss() as sct:
        monitor = sct.monitors[1]     
        img = np.array(sct.grab(monitor))
        frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        mask = vision.preprocess(frame)
        mouse_pos = mouse_control.get_mouse_pos()
        targets, can_shoot = vision.find_targets(mask, mouse_pos)
        closest = vision.closest_to_mouse(targets, mouse_pos)
        if closest != (-1, -1):
            dx = closest[0] - mouse_pos[0]
            dy = closest[1] - mouse_pos[1]
            if can_shoot > 0:
                mouse_control.mouse_click()
            else:
                mouse_control.move_mouse_smooth(dx, dy)
    return