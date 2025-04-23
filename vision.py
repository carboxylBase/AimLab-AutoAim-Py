import cv2
import math

def preprocess(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (82, 199, 118), (97, 255, 255))
    return mask

def find_targets(mask, mouse_pos):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    results = []
    res = -1
    for cnt in contours:
        if len(cnt) < 4: continue
        rect = cv2.boundingRect(cnt)
        if rect[2] * rect[3] < 50: continue
        cx, cy = rect[0] + rect[2] // 2, rect[1] + rect[3] // 2
        results.append((cx, cy))
        if cv2.pointPolygonTest(cnt, mouse_pos, False) > 0: res = 1
    return results, res

def closest_to_mouse(centers, mouse_pos):
    if not centers: return (-1, -1)
    return min(centers, key=lambda c: math.hypot(c[0] - mouse_pos[0], c[1] - mouse_pos[1]))
