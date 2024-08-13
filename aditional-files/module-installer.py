import pyautogui as gui
import time

def module_installer(Mod_name)->str:
    """
    main logic of the program
    """
    time.sleep(2)
    gui.hotkey("win","r")
    gui.write("cmd")
    gui.press("enter")
    time.sleep(1)

    Module_name_ = (f"pip install {Mod_name}")
    gui.write(Module_name_)
    gui.press("enter")


Module_name = input("Enter Module:")


module_installer(Mod_name=Module_name)