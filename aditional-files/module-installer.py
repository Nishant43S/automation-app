import pyautogui as gui
import time

def module_installer(Mod_name)->str:
    """
    main logic of the program
    """
    try:
        
        if Mod_name != "":
            time.sleep(2)
            gui.hotkey("win","r")
            gui.write("cmd")
            gui.press("enter")
            time.sleep(1)
        else:
            print("Enter module name...")

    except Exception as err:
        print("error...",err)
    Module_name_ = (f"pip install {Mod_name}")
    gui.write(Module_name_)
    gui.press("enter")


Module_name = input("Enter Module:")


module_installer(Mod_name=Module_name)