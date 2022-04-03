import pyautogui
import keyboard
import datetime
import tkinter
import time

SCREEN = tkinter.Tk()
SCREEN_WIDTH = SCREEN.winfo_screenwidth()
SCREEN_HEIGHT = SCREEN.winfo_screenheight()
cobblestone_farming = False

def string_typing(string):
    for letter in string:
        if letter == ' ': keyboard.press_and_release('space')
        else: keyboard.press_and_release(letter)
        time.sleep(0.1)
    keyboard.press_and_release('enter')
    
def enable_farming():
    print(" Cobblestone farming enabled\n")
    time.sleep(0.5)
    return True

def disable_farming():
    print(" Cobblestone farming disabled\n")
    time.sleep(0.5)
    return False
    
def reset_proxy():
    string_typing('thub')
    time.sleep(7)
    string_typing('tis')
    time.sleep(7)
    pyautogui.moveTo(SCREEN_WIDTH / 2, 0, duration = 0.3)
    time.sleep(1)
    keyboard.press_and_release('f')
    time.sleep(1)
    keyboard.press_and_release('f')

print("COBBLESTONE FARMER MACHINE STARTING                                                    \n",
      "- Press 'shift' to start farming                                                       \n",
      "- Press 'esc' to stop farming                                                          \n",
      "- Press 'r' to reset the cobblestone farm(it will reset automatically every 10 minutes)\n",
      "- You must put your keybinds on this way:                                              \n",
      "   'z': walk forward                                                                   \n",
      "   'k': destroy block                                                                  \n",
      "   't': open command chat                                                              \n",
      "   'f': toggle fullscreen mode                                                         \n",
      "                                                                                       \n")

while True:
    
    if keyboard.is_pressed('end'): break
    
    if keyboard.is_pressed('shift'): cobblestone_farming = enable_farming()
    
    if keyboard.is_pressed('esc'): cobblestone_farming = disable_farming()
        
    if cobblestone_farming:
        
        if (keyboard.is_pressed('r')) or ((datetime.datetime.now().minute in [00, 10, 20, 30, 40, 50]) and (datetime.datetime.now().second == 00)): reset_proxy()
        
        if datetime.datetime.now().second in [00, 30]: keyboard.press_and_release('space') 
        
        keyboard.press('z + k')
        time.sleep(0.1)
     
print("COBBLESTONE FARMER MACHINE CLOSING\n")
time.sleep(3)
