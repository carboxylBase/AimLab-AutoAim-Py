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
import shutil
import matplotlib.pyplot as plt

folder_path = 'measure/src'

print("Push 'S' to start.")

if not os.path.exists('measure/src'):
    os.makedirs('measure/src')

while True:
    if keyboard.is_pressed('a'):
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
        os.makedirs(folder_path)

        result = []

        step = 1
        for i in range(0, 1001, step):
            mouse_control.move_mouse_relative(step, 0)
            with mss.mss() as sct:
                monitor = sct.monitors[0]
                img = np.array(sct.grab(monitor))
            frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
            mask = vision.preprocess(frame)
            targets = vision.find_targets(mask)
            L_cx,L_cy,L_r = 100000,0,0
            for cx, cy, radius in targets:
                if cx < L_cx:
                    L_cx,L_cy,L_r = cx,cy,radius
            cv2.circle(frame, (int(L_cx), int(L_cy)), 5, (0, 0, 255), -1)
            text = f"({int(L_cx)}, {int(L_cy)}, {int(L_r)})"
            cv2.putText(frame, text, (int(L_cx)+10, int(L_cy)-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            # print(f"x: {L_cx} y: {L_cy} radius: {L_r}")
            result.append([i,L_cx])
            if i % 100 == 0: cv2.imwrite(f"measure/src/{i}.jpg", frame)
        
        for i in range(1,len(result)):
            result[i][1] = result[i][1] - result[0][1]
            result[i][1] = -result[i][1]
        result[0][1] = 0

        with open('measure/data.csv', 'w') as f:
            for cnt in result:
                f.write(f"{cnt[0]},{cnt[1]}\n")

        break