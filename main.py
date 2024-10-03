import numpy as np
import cv2
import pyautogui
import Quartz
import Quartz.CoreGraphics as CG
from PIL import Image
import keyboard
import sys

def get_window(window_title):
    for window in Quartz.CGWindowListCopyWindowInfo(
        Quartz.kCGWindowListOptionOnScreenOnly,
        Quartz.kCGNullWindowID,
    ):
        if window_title.lower() in window['kCGWindowOwnerName'].lower():
            return window





template_flipped = cv2.flip(cv2.imread('template.png',0),1)
template = cv2.imread('template.png',0)
switch = True
h,w = template.shape
method = cv2.TM_SQDIFF_NORMED
i=0



def screenshot_window(window):
    region = CG.CGRectMake(
    window['kCGWindowBounds']['X'],
    window['kCGWindowBounds']['Y']+400,
    window['kCGWindowBounds']['Width']-100,
    window['kCGWindowBounds']['Height']-650,
)

    cg_image = CG.CGWindowListCreateImage(
        region,
        CG.kCGWindowListOptionOnScreenOnly,
        window['kCGWindowOwnerPID'],
        CG.kCGWindowImageDefault,
    )

    image = Image.frombuffer(
        'RGBA',
        (CG.CGImageGetWidth(cg_image), CG.CGImageGetHeight(cg_image)),
        CG.CGDataProviderCopyData(CG.CGImageGetDataProvider(cg_image)),
        'raw',
        'BGRA',
        CG.CGImageGetBytesPerRow(cg_image),
        1,
    )
    return image


def click_left():
    pyautogui.click(window['kCGWindowBounds']['X']+200,window['kCGWindowBounds']['Y']+600)


def click_right():
    pyautogui.click(window['kCGWindowBounds']['X']+400,window['kCGWindowBounds']['Y']+600)

if __name__ == '__main__':
    window_title='Timberman'
    window = get_window(window_title)

    if window is None:
        print('Timberman might not be open yet try again after opening timberman')
        sys.exit()
    while True:
        i+=1
        if keyboard.is_pressed('esc'):
            break

        image = screenshot_window(window)
        if switch:
            image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
            img2 = image.copy()
            result = cv2.matchTemplate(img2, template, method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            print(min_val)
            location = min_loc
            bottom_right = (location[0] + w, location[1] + h)
            cv2.rectangle(img2,location,bottom_right,255,4)
            cv2.imwrite(f'result/frame{i}_location{location}_Min_val{min_val}.png',img2)
            if min_val>0.146:
                click_right()
        else:
            image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
            img2 = image.copy()
            result = cv2.matchTemplate(img2, template_flipped, method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            print(min_val)
            location = min_loc
            bottom_right = (location[0] + w, location[1] + h)
            cv2.rectangle(img2,location,bottom_right,255,4)
            cv2.imwrite(f'result/frame{i}_location{location}_Min_val{min_val}.png',img2)
            if min_val>0.146:
                click_left()
        if min_val<0.14 and min_val>0.06:
            switch = not switch
        cv2.destroyAllWindows()






