import pyautogui as pt
import keyboard as kb
import time

def cautare_google():
 if pt.locateOnScreen(r'C:\Users\Ed\Desktop\yty\google_search.png', confidence=0.7) != None:
    camp_google = pt.locateOnScreen(r'C:\Users\Ed\Desktop\yty\google_search.png', confidence=0.7)
    pt.click(camp_google)
    pt.write("https://www.youtube.com")
    pt.press('enter')
    time.sleep(10)
    camp_youtube = pt.locateOnScreen(r'C:\Users\Ed\Desktop\yty\youtube_search.png')
    pt.click(camp_youtube)
    pt.write("redlettermedia")
    pt.press('enter')
    time.sleep(10)
    canal = pt.locateOnScreen(r'C:\Users\Ed\Desktop\yty\canal.png')
    pt.click(canal)
    time.sleep(10)
    videos = pt.locateOnScreen(r'C:\Users\Ed\Desktop\yty\videos.png')
    pt.click(videos)
    time.sleep(10)
    while 1:
        pt.click(1200, 700)
        time.sleep(10)
        back = pt.locateOnScreen(r'C:\Users\Ed\Desktop\yty\back.png')
        pt.click(back)
        time.sleep(10)
        pt.click(1600, 700)
        time.sleep(10)
        back = pt.locateOnScreen(r'C:\Users\Ed\Desktop\yty\back.png')
        pt.click(back)
        time.sleep(10)
        pt.moveTo(1200, 700)
        pt.press('down')
        pt.press('down')
        pt.press('down')
        pt.press('down')
        pt.press('down')
        pt.press('down')
 else:
    print ("IMAGINEA NU SE AFLA PE ECRAN")

time.sleep(2)
cautare_google()