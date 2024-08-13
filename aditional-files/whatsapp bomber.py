import pywhatkit as kit
import random 
import pyautogui as gui
import time

Content_list = []
list_items_range = int(input("enter range:"))

if list_items_range <= 4:
    for li_ele in range(list_items_range):
        li_valu = input("enter items:")
        Content_list.append(li_valu)

        if li_valu == "0":
            break

else:
    print("enter 4 or less than 4 value")

number = int(input("Enter number:"))

msg = input("enter message:")  ##  message
count_down = int(input("starts in:")) ## starts in
limit_msg = int(input("Message Limit:")) ## message range

hour = int(input("enter hour:"))
minit = int(input("enter minit:"))

#######################################################################

message = msg+ " " + Content_list[0]
kit.sendwhatmsg(f"+91{number}",message,hour,minit)

try:
    time.sleep(count_down)

    #######  opening whats app  ############    
    gui.typewrite(message)
    gui.press("enter")
            ### loop ###
    for i in range(limit_msg+1):
        x = random.choice(Content_list)
        gui.write(msg+" "+x)
        gui.press("enter")
        #######  breaking the loop  ########

        if gui.move(0,0):
            break

    print(f"{limit_msg} message sended to {number}")

except Exception as err:
    print("something went wrong...")
    print(err)

