import pyautogui as gu
import random

import time

li = []

main_msg =input("enter main message:")
ran = int(input("enter range of list:"))

for i in range(ran):
    li_valu = input("enter items:")
    li.append(li_valu)
    if li_valu == str('0'):
        break

message_sending_limit = int(input("enter limit"))
x = int(input("enter starts in::"))

time.sleep(x)

for j in range(message_sending_limit+1):
    lis = random.choice(li)
    gu.write(main_msg+" "+lis)
    gu.press("enter")