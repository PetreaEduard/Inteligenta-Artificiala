import pyautogui as pt
import keyboard as kb
import time
import pynput as pp
mouse = pp.mouse.Controller()

def move_smooth(xm, ym, t):
    for i in range(t):
        if i < t/2:
            h = i
        else:
            h = t - i
        mouse.move(h*xm, h*ym)
        time.sleep(1/60)

def fish():
    timer = 1
    pt.click(button='right')
    while timer!=65:
        if pt.locateOnScreen(r'C:\Users\Ed\Desktop\fishingbot\splashes.png', confidence=0.7) != None:
            pt.click(button='right')
            timer = timer + 1
            time.sleep(1)
    store()
    fish()

def store():
    j = 0
    x = 743
    move_smooth(0, 5000, 30)
    pt.click(button='right')
    time.sleep(5)
    while j!=8:
        pt.moveTo(x, 906)
        pt.keyDown('shift')
        pt.click(button='right')
        x = x + 73
        time.sleep(1)
        j=j+1
    pt.keyUp('shift')
    pt.press('esc')
    move_smooth(0, -15, 10)
    pt.click(button='right')

time.sleep(10)
fish()
