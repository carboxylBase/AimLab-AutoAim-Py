import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import mouse_control
import vision
import keyboard
import time
import mss
import numpy as np
import cv2

print("Push 'S' to start.")

if not os.path.exists('measure/src'):
    os.makedirs('measure/src')

while True:
    if keyboard.is_pressed('a'):
        for i in range(0, 301, 50):
            mouse_control.move_mouse_relative(i, 0)
            with mss.mss() as sct:
                monitor = sct.monitors[0]
                img = np.array(sct.grab(monitor))
            frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
            mask = vision.preprocess(frame)
            targets = vision.find_targets(mask)
            for cx, cy, radius in targets:
                cv2.circle(frame, (int(cx), int(cy)), 5, (0, 0, 255), -1)
                text = f"({int(cx)}, {int(cy)}, {int(radius)})"
                cv2.putText(frame, text, (int(cx)+10, int(cy)-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                print(f"x: {cx} y: {cy} radius: {radius}")
            cv2.imwrite(f"measure/src/{i}.jpg", frame)
            print('\n')
            time.sleep(0.3)
