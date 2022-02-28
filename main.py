import keyboard as k
import time as tm
import pyautogui as p
import datetime as d
import tkinter as tk

SCREEN = tk.Tk()
SCREEN_WIDTH = SCREEN.winfo_screenwidth()
cobblestone_farming = False

def string_typing(string):
    for letter in string:
        k.press_and_release(letter)
        tm.sleep(0.1)
    k.press_and_release('enter')
    
def enable_farming():
    print(" Cobblestone farming enabled")
    tm.sleep(0.5)
    return True

def disable_farming():
    print(" Cobblestone farming disabled")
    tm.sleep(0.5)
    return False
    
def reset_farming():
    string_typing('thub')
    tm.sleep(5)
    string_typing('tis')
    tm.sleep(5)
    p.moveTo( SCREEN_WIDTH/2, 0, duration = 0.3 )
    tm.sleep(2)
    k.press_and_release('f')
    tm.sleep(2)
    k.press_and_release('f')

print("COBBLESTONE FARMER MACHINE STARTING \n",
      "- Press 'shift' to start farming \n",
      "- Press 'esc' to stop farming \n",
      "- Press 'r' to reset the cobblestone farm(it will reset automatically every 10 minutes) \n",
      "- You must put your keybinds on this way: \n",
      "  - 'z': walk forward \n",
      "  - 'k': destroy block \n",
      "  - 't': open command chat \n",
      "  - 'f': toggle fullscreen mode \n",
      "\n")

while True:
    
    if k.is_pressed('end'): break
    
    if k.is_pressed('shift'): cobblestone_farming = enable_farming()
    
    if k.is_pressed('esc'): cobblestone_farming = disable_farming()
        
    if ( k.is_pressed('r') ) or (
        (d.datetime.now().minute in [00, 10, 20, 30, 40, 50]) and
        (d.datetime.now().second == 00)
                                ): reset_farming()
        
    if cobblestone_farming:
        k.press('z + k')
        tm.sleep(0.1)
        
print("\nCOBBLESTONE FARMER MACHINE CLOSING \n")
tm.sleep(3)
