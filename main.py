import ctypes
import cv2
import numpy as np
import time
import math
import mss
from ctypes import wintypes

MOUSEEVENTF_MOVE = 0x0001
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004

class MOUSEINPUT(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong))]

class INPUT(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("mi", MOUSEINPUT)]

def send_input(dx, dy, flags):
    extra = ctypes.c_ulong(0)
    mi = MOUSEINPUT(dx, dy, 0, flags, 0, ctypes.pointer(extra))
    input_struct = INPUT(0, mi)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(input_struct), ctypes.sizeof(input_struct))

def move_mouse_relative(dx, dy):
    send_input(int(dx), int(dy), MOUSEEVENTF_MOVE)

def move_mouse_smooth(dx, dy, steps=1, delay=0):
    for _ in range(steps):
        move_mouse_relative(dx / steps, dy / steps)

def mouse_click():
    send_input(0, 0, MOUSEEVENTF_LEFTDOWN)
    send_input(0, 0, MOUSEEVENTF_LEFTUP)

def get_mouse_pos():
    pt = wintypes.POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))
    return pt.x, pt.y

def preprocess(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (82, 199, 118), (97, 255, 255))
    return mask

def find_targets(mask,mouse_pos):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    results = []
    res = -1
    for cnt in contours:
        if len(cnt) < 4: continue
        rect = cv2.boundingRect(cnt)
        if rect[2] * rect[3] < 50: continue
        cx, cy = rect[0] + rect[2] // 2, rect[1] + rect[3] // 2
        results.append((cx, cy))
        if cv2.pointPolygonTest(cnt,mouse_pos,False) > 0: res = 1
    return results,res

def closest_to_mouse(centers, mouse_pos):
    if not centers: return (-1, -1)
    return min(centers, key=lambda c: math.hypot(c[0] - mouse_pos[0], c[1] - mouse_pos[1]))

auto_aim = False
start_time = None
AUTO_AIM_DURATION = 70000

cv2.namedWindow("Screen", cv2.WINDOW_KEEPRATIO)
cv2.namedWindow("Mask", cv2.WINDOW_KEEPRATIO)

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
            if (time.time() - start_time) * 1000 >= AUTO_AIM_DURATION:
                auto_aim = False

            begin = time.time()
            img = np.array(sct.grab(monitor))
            frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
            mask = preprocess(frame)
            mouse_pos = get_mouse_pos()
            targets,can_shoot = find_targets(mask,mouse_pos)
            
            closest = closest_to_mouse(targets, mouse_pos)
            if (closest != (-1,-1)):
                dx = closest[0] - mouse_pos[0]
                dy = closest[1] - mouse_pos[1]
                dist = math.hypot(dx, dy)

                if can_shoot > 0:
                    mouse_click()
                else:
                    move_mouse_smooth(dx, dy)

cv2.destroyAllWindows()