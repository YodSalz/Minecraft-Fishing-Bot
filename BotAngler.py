from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
import pyautogui
import time
import win32api
import win32con
import keyboard
import operator
import os
import win32gui

#for mouse position finding:
#from PIL import ImageGrab
#from functools import partial
#ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
#import pyautogui
#pyautogui.displayMousePosition()

def finding_pixeValue_start():
    print('move the mouse to the start of the black rope (in right hand) and then click (open inventory to do so)')
    print('u need to hit a black pixel in order for it to work (the rbg will be 0, 0, 0 later, else it will restart!')
    while True:
        if win32api.GetKeyState(0x01) == -128 or win32api.GetKeyState(0x01) == -127:
            global position
            position = pyautogui.position() #Tuple Point(X|Y)
            print(position[0]) #int
            print(position[1]) #int
            print('close inventory for checking color(in 2 seconds)!')
            time.sleep(2)
            if ImageGrab.grab().getpixel(position) == (0,0,0):
                break    
            else:
                print('rgb value of rope (must be 0,0,0!!!):')
finding_pixeValue_start()

def find_area_of_redThing(position):
    print('finding the area now...')
    x_pixel_testing = position[0]
    y_pixel_testing = position[1]
    searching = True
    screenshot = ImageGrab.grab()
    while searching:
        x_pixel_testing = x_pixel_testing-1
        for e in range(0,10):
            y = y_pixel_testing-5+e
            pixel_tested = screenshot.getpixel((x_pixel_testing, y))
            if pixel_tested == (0,0,0):
                y_pixel_testing = y
                break
            elif e == 8:
                searching = False
            #now the two positions are at the furthest point --> search for red
    global red_top
    red_top = (x_pixel_testing,y_pixel_testing)
find_area_of_redThing(position)
print('fishing starts in 2 seconds...')
time.sleep(2)

light_rgb = (208,41,41)
dark_rgb = (132,20,20)

def dowalk(boole):
    if not boole:
        keyboard.press('d')
        time.sleep(1.5)
        keyboard.release('d')
    if boole:
        keyboard.press('a')
        time.sleep(1.5)
        keyboard.release('a')
    time.sleep(0.3)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
    time.sleep(1.3)
    
def drawRect(x,y):
    print('not functioning')

def fish(area):
    fishings = 0
    right = False
    clear = lambda: os.system('cls')
    clear()
    screenshotarea = (red_top[0]-10,red_top[1]-3,red_top[0]+16,red_top[1]+34)
    while True: #actual fishing begins here    
        red_part_value = 0
        screenshot = ImageGrab.grab(bbox=screenshotarea)
        #screenshot.show()
        for z in range(0,30):
            rgb_now = screenshot.getpixel((area[0]-screenshotarea[0],area[1]+z-screenshotarea[1]))
            #pyautogui.moveTo(area[0],area[1]+z)
            if rgb_now[0]/(rgb_now[1]+1) > 2.2 and rgb_now[0]/(rgb_now[2]+1) > 2.2:
                red_part_value = red_part_value + 1
            #print(red_part_value)
        print(red_part_value) #treshhold
        if red_part_value < 1:
            #dofish()
            #time.sleep(1)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
            time.sleep(0.01)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
            if fishings < 7:
                fishings = fishings + 1
                time.sleep(0.6)
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
                time.sleep(0.01)
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
                clear = lambda: os.system('cls')
                clear()
                print('fishings:')
                print(fishings)
                print('-----------------')
                print('treshhold value:')
                time.sleep(1.3)
            else:
                dowalk(right)
                right = operator.not_(right)
                fishings = 0
fish(red_top)