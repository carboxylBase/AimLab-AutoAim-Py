import cv2
import math
import config

def preprocess(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (82, 199, 118), (97, 255, 255))
    return mask

def find_targets(mask):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    results = []
    for cnt in contours:
        if len(cnt) < 4: continue
        (cx, cy), radius = cv2.minEnclosingCircle(cnt)
        if radius < config.MIN_AREA : continue
        results.append((cx, cy,radius))
    return results
