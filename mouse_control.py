import ctypes
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
    
driver = ctypes.CDLL(r'lib/MouseControl.dll')

def send_input(dx, dy, flags):
    extra = ctypes.c_ulong(0)
    mi = MOUSEINPUT(dx, dy, 0, flags, 0, ctypes.pointer(extra))
    input_struct = INPUT(0, mi)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(input_struct), ctypes.sizeof(input_struct))

def move_mouse_relative(dx, dy):
    driver.move_R(int(dx), int(dy))
    # send_input(int(dx), int(dy), MOUSEEVENTF_MOVE)

def move_mouse_smooth(dx, dy, steps=1, delay=0):
    for _ in range(steps):
        move_mouse_relative(dx / steps, dy / steps)

def mouse_click():
    driver.click_Left_down()
    driver.click_Left_up()
    # send_input(0, 0, MOUSEEVENTF_LEFTDOWN)
    # send_input(0, 0, MOUSEEVENTF_LEFTUP)

def get_mouse_pos():
    pt = wintypes.POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))
    return pt.x, pt.y
