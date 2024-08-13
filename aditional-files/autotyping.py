import pyautogui as gui
import time

Text = input("Enter Message::")
Timer = input("Enter Timer::")

time.sleep(int(Timer))

gui.write(Text)
