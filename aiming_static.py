import mouse_control
import vision
import mss
import cv2
import numpy as np
import win32gui

def run(aimlab_tb_hwnd):
    left, top, right, bottom = win32gui.GetClientRect(aimlab_tb_hwnd)
    left_screen, top_screen = win32gui.ClientToScreen(aimlab_tb_hwnd, (left, top))
    right_screen, bottom_screen = win32gui.ClientToScreen(aimlab_tb_hwnd, (right, bottom))
    with mss.mss() as sct:
        monitor = {"left": left_screen, "top": top_screen, "width": right_screen - left_screen, "height": bottom_screen - top_screen}
        img = np.array(sct.grab(monitor))
        frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        mask = vision.preprocess(frame)
        mouse_pos = mouse_control.get_mouse_pos()
        mouse_pos = list(mouse_pos)
        mouse_pos[0] = mouse_pos[0] - left_screen
        mouse_pos[1] = mouse_pos[1] - top_screen
        targets, can_shoot = vision.find_targets(mask, mouse_pos)
        closest = vision.closest_to_mouse(targets, mouse_pos)

        if closest != (-1, -1):
            dx = closest[0] - mouse_pos[0]
            dy = closest[1] - mouse_pos[1]
            if can_shoot > 0:
                mouse_control.mouse_click()
            else:
                mouse_control.move_mouse_smooth(dx, dy)