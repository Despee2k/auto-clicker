import pyautogui
import keyboard
import time

# Initialization
preset = 'assets/presets.png'
short = 'assets/short.png'
apply = 'assets/apply.png'
okay = 'assets/okay.png'

pyautogui.moveTo(100,500)
pyautogui.click()

presetLoc = pyautogui.locateOnScreen(preset)
presetPoint = pyautogui.center(presetLoc)
presetX, presetY = presetPoint
if(presetLoc):
    time.sleep(1)
    pyautogui.click(presetX, presetY, clicks=2, interval=0.5)
    
    shortLoc = pyautogui.locateOnScreen(short)
    shortPoint = pyautogui.center(shortLoc)
    shortX, shortY = shortPoint
    if(shortLoc):
        time.sleep(1)
        pyautogui.click(shortX, shortY, clicks=2, interval=0.5)
        
        applyLoc = pyautogui.locateOnScreen(apply)
        applyPoint = pyautogui.center(applyLoc)
        applyX, applyY = applyPoint
        if(applyLoc):
            time.sleep(2)
            pyautogui.click(applyX, applyY + 10, clicks=2, interval=0.5)
            
            okayLoc = pyautogui.locateOnScreen(okay)
            okayPoint = pyautogui.center(okayLoc)
            okayX, okayY = okayPoint
            if(okayLoc):
                time.sleep(2)
                pyautogui.click(okayX, okayY)

keyboard.read_key()
if keyboard.is_pressed('p'):
    print("Exiting...")
    quit()
    
    