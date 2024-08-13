import ttkbootstrap as ttkb
from tkinter import *
import tkinter.messagebox as tkmsg
from ttkbootstrap.constants import *
import customtkinter as Ctk
import pywhatkit as kit
import pyautogui as gui
import time
from time import strftime
import pyttsx3
import phonenumbers
from phonenumbers import timezone,geocoder
from phonenumbers import carrier
import random
import numpy
import smtplib


#############################  Digital  time clock

def time__get():
    time_str = strftime("%H : %M : %S %p  ")
    Real_time_clock.config(text=time_str)
    Real_time_clock.after(1000,time__get)

root = ttkb.Window(themename="vapor")

##############  bottom functions 

### google

def google_src():
    x = Google_search_box.get()
    try:
        kit.search(x)
    except Exception as err :
        tkmsg.showwarning("something went wrong", err)
        
### youtube

def youtube_src():
    x = youtube_search_box.get()
    try:
         kit.playonyt(x)
    except Exception as err :
        tkmsg.showwarning("ඞ something went wrong",f"{err}")
        
def Install_module():
    mod_name = Module_variable.get()
    mod_name = mod_name.strip()
    if mod_name == "":
        tkmsg.showwarning("ඞ error...",
                          "enter module name"
                          )
    else:
        try:
            gui.hotkey('win','r')
            gui.write("cmd")
            gui.press("enter")
            time.sleep(1)
            gui.write("pip install " + mod_name)
            gui.press("enter") 

        except Exception as err:
            tkmsg.showwarning("something went wrong",err)

##############################################################

#######  body section functions

#########  simple message spamer


if __name__ == "__main__":
    def simple_msg_func():

        a = MESSAGE.get()
        b = MSG_Limit.get()
        c = COUNT_down.get()              ####  variables
        done_ = done_symbol.get()

        if __name__ == "__main__":
            if a.strip() == "" or b == 0 or c == 0:
                done_symbol.set("fill all fieds")
                tkmsg.showwarning("error","🤬 fill all fields")
                return False
            else:
            
                try:
                    time.sleep(c)
                    for i in range(b+1):
                        gui.write(a)
                        gui.press("enter")
                        if gui.move(0,0):
                            break
                        
                    eng = pyttsx3.init()                 ## speak message
                    eng.say(f"{b} message Delivered")
                    eng.runAndWait()

                    done_symbol.set("✓")  ## done symbol text
                    return True
                except:
                    tkmsg.showwarning("error","something went wrong")


###################################################################################

###########  phone number details function

if __name__=="__main__":
    def get_Number_Information():
        phone_num = Ph_number_var.get()
        cuntry_code_num = Country_code_var.get()
        try:
            if phone_num :

                timezone_result = TimeZone_variable.get()
                carrier_result = Carrier_variable.get()
                country_result = Country_variable.get()

                Ph_num = cuntry_code_num+phone_num
                phone_number_result = phonenumbers.parse(Ph_num) 

                timezone_result = timezone.time_zones_for_number(phone_number_result)
                carrier_result = carrier.name_for_number(phone_number_result,"en")
                country_result = geocoder.description_for_number(phone_number_result,"en")

                TimeZone_variable.set(timezone_result)
                Carrier_variable.set(carrier_result)
                Country_variable.set(country_result)


            else:
                tkmsg.showwarning("error","Enter valid number")
                return False
        except Exception as er:
            tkmsg.showwarning("error",f"something went wrong\n{str(er)}")



#####################################################################################################################################################################################

############  whatsapp number bomber

##3 listbox functions

def Insert_func_whatsapp():
    insert_element = whatsapp_listbox_entry.get()

    if insert_element and len(whatsapp_listbox.get(0, END)) < 5:

        eng = pyttsx3.init()                 ## speak message
        eng.say(f"{insert_element} inserted")
        eng.runAndWait()

        whatsapp_listbox.insert(END,insert_element)
        whatsapp_listbox_entry.delete(0, END)

    else:
        tkmsg.showwarning("error","unable to enter")


def Delete_func_whatsapp():
    whatsapp_listbox.delete(0)

def Delete_1_func():
    selected_item = whatsapp_listbox.curselection()
    if selected_item:
        whatsapp_listbox.delete(selected_item)


def Send_WhatS_app_message():
    if __name__=="__main__":
        try:
            Num_ = Phone_number_whatsapp.get()
            Hour_ = Hours_whatsapp.get()
            Minit_ = Minits_whatsapp.get()

            _message_get = Front_message_whatsapp.get()+" "+whatsapp_listbox.get(0)
            kit.sendwhatmsg(f"+91{Num_}",_message_get,Hour_,Minit_)
            gui.write(_message_get)
            gui.press("enter")

                     ###### setting range
            tim_err = CountDown_whatsapp.get()
            time.sleep(tim_err)
            lim_ = Msg_limit_whatsapp.get()
            for iii in range(lim_+1):

                abc = numpy.arange(5)
                xp = whatsapp_listbox.get(random.choice(abc))
                gui.write(Front_message_whatsapp.get()+" "+xp)
                gui.press("enter")
                if gui.move(0,0):
                    eng = pyttsx3.init()                 ## speak message
                    eng.say(f"whatsapp Bomber stop")
                    eng.runAndWait()
                    break

            eng = pyttsx3.init()                 ## speak message
            eng.say(f"whatsapp Bomber has sent {lim_+1} Messages")
            eng.runAndWait()

        except Exception as err:
            tkmsg.showwarning("error",f"something went wrong\n{err}")




##################  menu bar

############  menubar functions

def Developer():
    tkmsg.showinfo("developer","App creater: Nishant Maity\nDesigner: Nishant Maity")

def auto_typing_info():
    tkmsg.showinfo("AutoTyping",
                   """
            It will type text Automaticaly
            which is inside in Text Box
                    """)
    
def simple_spammer_info():
        tkmsg.showinfo("Simple Spammer",
                   """
            It will spam text or message
            n number of times
                    """)

def phone_number_infor():
    tkmsg.showinfo("Phone number information",
                   """
            It will gives you any Country 
            Number Number information
                    """)

def Email_sender_info():
    tkmsg.showinfo("Email Sender",
                   """
            It will Send Mail to 
            Multiple people
                    """)

def Youtube_search_info():
    tkmsg.showinfo("Youtube",
                   """
            It will Open YouTube
            and play video what
            you enter
                    """)
    
def Google_search_info():
    tkmsg.showinfo("Google",
                   """
            It will Open Google
            and search what
            you enter
                    """)    

def Module_installer_info():
        tkmsg.showinfo("Module Installer",
                   """
            It will install 
            Module what you enter
                    """)

def Term_conditions():
     tkmsg.showinfo("Terms and conditions",
                   """
            Only for educational purposes
            Don't missuse it
                    """)
     
############  app information

def lang_use():
    tkmsg.showinfo("Language used",
                   """
            app is developed on python
            programing language
                    """)

def module_use():
        tkmsg.showinfo("modules used",
                   """
                    1> tkinter Gui
                    2> ttkbootstrap Gui
                    3> Custom tkinter Gui
                    4> time and strftime Displaying time    
                    5> smtplib Email    
                    6> PhoneNumbers 
                    7> pyautogui automation    
                    8> pywhatkit automation    
                    9> pyttsx3 speak    
                    """)

Menu_bar = Menu(root)

services = Menu(Menu_bar)
services['bg']='#303841'
services['fg']='#d3d6db'

Menu_bar.add_command(label="Developer",command=Developer)
Menu_bar.add_command(label="Terms & condition",command=Term_conditions)

services.add_command(label="WhatsApp Spammer")
services.add_command(label="Simple Spammer",command=simple_spammer_info)
services.add_command(label="Phone N.o Info",command=phone_number_infor)
services.add_command(label="Email Sender",command=Email_sender_info)
services.add_command(label="Auto Typing",command=auto_typing_info)
services.add_command(label="Youtube",command=Youtube_search_info)
services.add_command(label="Google",command=Google_search_info)
services.add_command(label="Module installer",command=Module_installer_info)

Menu_bar.add_cascade(label="Services",menu=services)

app_info = Menu(Menu_bar)
app_info['bg']='#303841'
app_info['fg']='#d3d6db'

app_info.add_command(label="Language used",command=lang_use)
app_info.add_command(label="Module used",command=module_use)

Menu_bar.add_cascade(label="app info",menu=app_info)
Menu_bar.add_command(label="Exit App",command=quit)


root.config(menu=Menu_bar)

############################################################################################################################################################################

########   email automation function

#######  insert delete function of list box


def Email_insert_btn():
    email_ent = Recivers_name_entry_box.get()
    if email_ent:
        Reciver_list_box.insert(END,email_ent)
        Recivers_name_entry_box.delete(0, END)
    else:
        tkmsg.showwarning("error","enter email")

def Email_delete_btn():
   Reciver_list_box.delete(0)
  


def Email_delete_curent_btn():
    del_current_email = Reciver_list_box.curselection()
    if del_current_email:
        Reciver_list_box.delete(del_current_email)

if __name__=="__main__":
    def Send_mail_smtp():

        Sender_userMail = email_sender_name.get()
        Sender_password = email_password_box.get()

        Subject_Email = subject_label_email_box.get()
        Body_of_Email = body_text_eamil_area.get("1.0",END)

        try:
            reciver_list_box_ = Reciver_list_box.get(0,END)
           
            server = smtplib.SMTP("smtp.gmail.com",587)
            server.starttls()
            server.login(Sender_userMail,Sender_password)
            server.sendmail(
                    Sender_userMail, reciver_list_box_, 
                    f"Subject: {Subject_Email}\n{Body_of_Email}"
                    )
            
            eng = pyttsx3.init()                 ## speak message
            eng.say(f"email sended")
            eng.runAndWait()

        except Exception as eor:
            tkmsg.showwarning("error",f"something went wrong\n{eor}")

####################################################################################################################################################################################################3

##########  autotyping

if __name__=="__main__":

    def automatic_type():
        del_time_get = strating_time_var.get()
        get_typed_text = Text_area.get("1.0",END)
        try:
            if del_time_get :
                time.sleep(del_time_get)
                gui.write(get_typed_text)

                
            eng = pyttsx3.init()                 ## speak message
            eng.say(f"text successfully typed")
            eng.runAndWait()

        except Exception as eor:
            tkmsg.showwarning("error",f"something went wrong\n{eor}")
    
#####################################################################################################################################################################################################################################################################################################################

####### Top frame

#####################  main title

Top_frame = Frame(
        root,
        width = 1594,height=49
)
Top_frame.pack(side=TOP,pady=1,padx=0,anchor=NW)

top_frame_content = ttkb.LabelFrame(Top_frame,
                                    bootstyle="dark",width=954
                                    )
top_frame_content.pack_propagate(False)
top_frame_content.pack(side=TOP,padx=0)
Main_heading = ttkb.Label(top_frame_content,
                          text="Auto🤖 Magic ",
                          foreground="#fe346e",
                          font=("cobel",20)
                          )

Main_heading.grid(row=0,column=0,sticky=W,padx=59,pady=4)


Label(top_frame_content,text="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ").grid(row=0,column=1)  ## gap between clock and app name

Real_time_clock = ttkb.Label(
            top_frame_content,
            font=("ds-digital",13),
            foreground="cyan"
    )

Real_time_clock.grid(row=0,column=2)

time__get()

clock_border = ttkb.Sizegrip(
        top_frame_content,
        bootstyle="success"
)
clock_border.grid(row=0,column=3)
x=ttkb.Label(top_frame_content,text="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ").grid(row=0,column=4,sticky=W)

#################################################################################################################################################################################################################

################    Body frame


Body_frame = ttkb.Frame(
        root,
        width=1675,height=653
                                                    ############  main body
)
Body_frame.pack(side=TOP,pady=26,fill=Y,ipadx=3,ipady=9,padx=16,anchor=NW)
Body_frame.pack_propagate(True)


############main body frame

###########################################################

####################  left side frame row 0 column 0

########  message spammer  simple

### text fields

Simple_msg_spammer = ttkb.LabelFrame(
            Body_frame,
            text="Simple spammer",
            bootstyle="info"
)

Simple_msg_spammer.grid(row=0,column=0,padx=6,pady=8,ipadx=5,ipady=3)
Simple_msg_spammer.pack_propagate(True)


Message = ttkb.Label(
        Simple_msg_spammer,text="Message",
        font=("ds-digital",13),
        bootstyle='light'
    )
Message.grid(row=0,column=0,sticky=W,padx=7,pady=5)


msg_limit = ttkb.Label(
        Simple_msg_spammer,text="Limit",
        font=("ds-digital",13),
        bootstyle='light'
    )
msg_limit.grid(row=1,column=0,sticky=W,padx=7,pady=5)


count_down = ttkb.Label(
        Simple_msg_spammer,text="Countdown",
        font=("ds-digital",13),
        bootstyle='light'
    )
count_down.grid(row=2,column=0,sticky=W,padx=7,pady=5)

#### enter fields

#####  enter fields variables

MESSAGE = StringVar()
MSG_Limit = IntVar()
COUNT_down = IntVar()

msg_entry_box = ttkb.Entry(
            Simple_msg_spammer,
            bootstyle="info",
            font=("ds-digital",13),
            width=22,textvariable=MESSAGE
)
msg_entry_box.grid(row=0,column=1,sticky=W,padx=7,pady=5)

limit_entry_box = ttkb.Entry(
            Simple_msg_spammer,
            bootstyle="info",
            font=("ds-digital",13),
            width=22,textvariable=MSG_Limit
)
limit_entry_box.grid(row=1,column=1,sticky=W,padx=7,pady=5)

countdown_entry_box = ttkb.Entry(
            Simple_msg_spammer,
            bootstyle="info",
            font=("ds-digital",13),
            width=22,textvariable=COUNT_down
)
countdown_entry_box.grid(row=2,column=1,sticky=W,padx=7,pady=5)

##########  simple spammer button

simple_spam_btn_style = ttkb.Style()
simple_spam_btn_style.configure("info.TButton",font=("arial",12))

Simple_spam_btn = ttkb.Button(
                            Simple_msg_spammer,
                              text="send",
                              bootstyle='info',
                              width=9,style="info.TButton",
                              command=simple_msg_func
                )

Simple_spam_btn.grid(row=3,column=0,sticky=W,padx=7,pady=5,columnspan=2)


done_symbol = StringVar()

Done_symbol_text = ttkb.Label(
            Simple_msg_spammer,
            bootstyle="success",
            font=("ds-digital",14),
            textvariable=done_symbol
)
Done_symbol_text.grid(row=3,column=1,padx=7,pady=5)

################################################################################################

###############  body frame column 0 row 1

###########   phone number information getter

Phone_number_details = ttkb.LabelFrame(
            Body_frame,
            text="number information",
            bootstyle="info"
)

Phone_number_details.grid(row=1,column=0,padx=6,pady=8,ipadx=5,ipady=3)
Phone_number_details.pack_propagate(True)


Country_code_label = ttkb.Label(
        Phone_number_details,text="Country code",
        font=("ds-digital",13),
        bootstyle='light'
    )
Country_code_label.grid(row=0,column=0,sticky=W,padx=7,pady=5)


Number_message = ttkb.Label(
        Phone_number_details,text="Enter Number",
        font=("ds-digital",13),
        bootstyle='light'
    )
Number_message.grid(row=1,column=0,sticky=W,padx=7,pady=5)

###############   phone number variable

Ph_number_var = StringVar()
Country_code_var = StringVar()

Country_code_var.set("+91")
# entry box

Countrycode_entry_box = ttkb.Entry(
            Phone_number_details,
            bootstyle="info",
            font=("ds-digital",13),
            width=20,textvariable=Country_code_var
)
Countrycode_entry_box.grid(row=0,column=1,sticky=W,padx=7,pady=5)



number_entry_box = ttkb.Entry(
            Phone_number_details,
            bootstyle="info",
            font=("ds-digital",13),
            width=20,textvariable=Ph_number_var
)
number_entry_box.grid(row=1,column=1,sticky=W,padx=7,pady=5)


############  labels details of number

Label(
    Phone_number_details
        ).grid(row=2,column=0,sticky=W,padx=7,pady=5)   ### empty field phone numbers

###############################

Timezone_label = ttkb.Label(
        Phone_number_details,text="Time Zone",
        font=("carbel",13),
        bootstyle='light'
    )
Timezone_label.grid(row=3,column=0,sticky=W,padx=7,pady=5)

Carrier_label = ttkb.Label(
        Phone_number_details,text="Carrier",
        font=("carbel",13),
        bootstyle='light'
    )
Carrier_label.grid(row=4,column=0,sticky=W,padx=7,pady=5)


Country_label = ttkb.Label(
        Phone_number_details,text="Country",
        font=("carbel",13),
        bootstyle='light'
    )
Country_label.grid(row=5,column=0,sticky=W,padx=7,pady=5)

##################################  output field phone number

#########   variables

TimeZone_variable = StringVar()
Carrier_variable = StringVar()
Country_variable = StringVar()

Timezone_output = ttkb.Label(
        Phone_number_details,textvariable=TimeZone_variable,
        font=("carbel",13),
        bootstyle='light'
    )
Timezone_output.grid(row=3,column=1,sticky=W,padx=7,pady=5)

Carrier_output = ttkb.Label(
        Phone_number_details,textvariable=Carrier_variable,
        font=("carbel",13),
        bootstyle='light'
    )
Carrier_output.grid(row=4,column=1,sticky=W,padx=7,pady=5)

Country_output = ttkb.Label(
        Phone_number_details,textvariable=Country_variable,
        font=("carbel",13),
        bootstyle='light'
    )
Country_output.grid(row=5,column=1,sticky=W,padx=7,pady=5)

Label(
    Phone_number_details
        ).grid(row=6,column=0,sticky=W,padx=7,pady=11)   ### empty field phone numbers

###########################  phone information button

Phone_info_button = ttkb.Button(
            Phone_number_details,
            text="Get detail",
            bootstyle="danger,outline",
            width=49,command=get_Number_Information
)
Phone_info_button.grid(row=7,column=0,padx=3,sticky=W,pady=5,columnspan=2,ipady=3) 

#########################################################################################################################################################################

#################  whatsapp number bomber

##############   whatsup bomber frame

############  setting frame

whatsapp_number_spammer = ttkb.LabelFrame(
            Body_frame,
            text="Whatsapp Number spammer",
            bootstyle="success"
)

whatsapp_number_spammer.grid(row=0,column=1,padx=6,pady=8,ipadx=5,ipady=3,rowspan=2)
whatsapp_number_spammer.pack_propagate(True)



##########  creating list box

whatsapp_listbox = Listbox(
        whatsapp_number_spammer,
        width=16,
        height=5,                                 ######## list box whatsapp
        font=("arial",11)
)
whatsapp_listbox.grid(row=0,column=0,padx=4,pady=5)


whatsapp_listbox_entry_label = Label(
        whatsapp_number_spammer,
        text="Enter items",font=('arial',13),
)

whatsapp_listbox_entry_label.grid(row=1,column=0,sticky=W,padx=4,pady=5)

whatsapp_listbox_entry = ttkb.Entry(
        whatsapp_number_spammer,
        font=('arial',13),
        width=12,bootstyle='danger'

)

whatsapp_listbox_entry.grid(row=1,column=1,padx=4,pady=5)

############   list box insert delete buttons frame

whatsup_custoum_frame = Frame(whatsapp_number_spammer)
whatsup_custoum_frame.grid(row=0,column=1,padx=4,pady=5)

Insert_button_whatsapp = ttkb.Button(
            whatsup_custoum_frame,text="Insert",
            width=13,command=Insert_func_whatsapp        
)

Insert_button_whatsapp.pack(pady=2)

Delete_button_whatsapp = ttkb.Button(
            whatsup_custoum_frame,text="Delete",
            width=13,command=Delete_func_whatsapp        
)

Delete_button_whatsapp.pack(pady=2)

delete_1_button_whatsapp = ttkb.Button(
            whatsup_custoum_frame,text="Delete sle",
            width=13,command=Delete_1_func        
)

delete_1_button_whatsapp.pack(pady=2)

############################################################

#######  labels and entry fields

######   starts from row 2 column 0

Whatsapp_number_label = Label(
        whatsapp_number_spammer,
        text="Phone Number",font=('arial',13),
)

Whatsapp_number_label.grid(row=2,column=0,sticky=W,padx=4,pady=5)

Whatsapp_msg_label = Label(
        whatsapp_number_spammer,
        text="Main Message",font=('arial',13),
)

Whatsapp_msg_label.grid(row=3,column=0,sticky=W,padx=4,pady=5)

Starts_timer_label = Label(
        whatsapp_number_spammer,
        text="Countdown",font=('arial',13),
)

Starts_timer_label.grid(row=4,column=0,sticky=W,padx=4,pady=5)

message_Limit_label = Label(
        whatsapp_number_spammer,
        text="Set Limit",font=('arial',13),
)

message_Limit_label.grid(row=5,column=0,sticky=W,padx=4,pady=5)


##############   time label  ############

Time_hour_minit = Label(
        whatsapp_number_spammer,
        text=" Sending Time enter H/M ",
        font=('carbel',13),
)
Time_hour_minit.grid(row=6,column=0,padx=4,pady=5,columnspan=2)

Whatsapp_Hour_label = Label(
        whatsapp_number_spammer,
        text="Enter Hour",font=('carbel',13),
)

Whatsapp_Hour_label.grid(row=7,column=0,sticky=W,padx=4,pady=5)

Whatsapp_Minit_label = Label(
        whatsapp_number_spammer,
        text="Enter Minute",font=('Carbel',13),
)

Whatsapp_Minit_label.grid(row=8,column=0,sticky=W,padx=4,pady=5)

Label(whatsapp_number_spammer
      ).grid(row=9,column=0,sticky=W,padx=4,pady=5)  ### blank fields


#####################################################################

############  whatsapp spammer entry box  

### variables of whats app spammer

Phone_number_whatsapp = IntVar()
Front_message_whatsapp = StringVar()
CountDown_whatsapp = IntVar()
Msg_limit_whatsapp = IntVar()

### time variables

Hours_whatsapp = IntVar()
Minits_whatsapp = IntVar()

##########  starts from row 2

PhoneNumber_Whatsapp_box = ttkb.Entry(
        whatsapp_number_spammer,
        bootstyle="danger",
        font=('Carbel',13),
        width=12,
        textvariable=Phone_number_whatsapp
)
PhoneNumber_Whatsapp_box.grid(row=2,column=1,padx=4,pady=5)

Front_msg_Whatsapp_box = ttkb.Entry(
        whatsapp_number_spammer,
        bootstyle="danger",
        font=('Carbel',13),
        width=12,
        textvariable=Front_message_whatsapp
)
Front_msg_Whatsapp_box.grid(row=3,column=1,padx=4,pady=5)

Ciuntdown_Whatsapp_box = ttkb.Entry(
        whatsapp_number_spammer,
        bootstyle="danger",
        font=('Carbel',13),
        width=12,
        textvariable=CountDown_whatsapp
)
Ciuntdown_Whatsapp_box.grid(row=4,column=1,padx=4,pady=5)

Limit_msg_Whatsapp_box = ttkb.Entry(
        whatsapp_number_spammer,
        bootstyle="danger",
        font=('Carbel',13),
        width=12,
        textvariable=Msg_limit_whatsapp
)
Limit_msg_Whatsapp_box.grid(row=5,column=1,padx=4,pady=5)

Hour_msg_Whatsapp_box = ttkb.Entry(
        whatsapp_number_spammer,
        bootstyle="danger",
        font=('Carbel',13),
        width=12,
        textvariable=Hours_whatsapp
)
Hour_msg_Whatsapp_box.grid(row=7,column=1,padx=4,pady=5)

Minit_msg_Whatsapp_box = ttkb.Entry(
        whatsapp_number_spammer,
        bootstyle="danger",
        font=('Carbel',13),
        width=12,
        textvariable=Minits_whatsapp
)
Minit_msg_Whatsapp_box.grid(row=8,column=1,padx=4,pady=5)

WhatsApp_msg_send_btn = Ctk.CTkButton(
        whatsapp_number_spammer,
        text="S E N D",
        width=198,
        command=Send_WhatS_app_message,
        font=("carbel",18)
)

WhatsApp_msg_send_btn.grid(row=9,columnspan=2,column=0,padx=4,pady=18)

########################################################################################################################################################################################################################

################   email sender  

##########  setting frame 

Email_automate = ttkb.LabelFrame(
            Body_frame,
            text="Email sender",
            bootstyle="warning"
)

Email_automate.grid(row=0,column=2,padx=6,pady=8,ipadx=5,ipady=3,columnspan=2)
Email_automate.pack_propagate(True)

###########   text section frame

email_text_area_frame = Frame(
        Email_automate,
)
email_text_area_frame.grid(row=0,column=0,padx=2,pady=2)

######################              test area frame email

#### list box of reciver 

Reciver_name_label = ttkb.Label(
        email_text_area_frame,
        text="Recivers",        
        font=('arial',8)

)
Reciver_name_label.grid(row=0,column=0,sticky=W,padx=3,pady=4)


Reciver_list_box = Listbox(
        email_text_area_frame,
        width=31,
        height=6                                        #####  listbox email
)
Reciver_list_box.grid(row=1,column=0,padx=3,pady=2)


#####  email list box variable

Recivers_name_entry_box = ttkb.Entry(
        email_text_area_frame,
        font=("arial",10),
        width=27,
        bootstyle="info",
                               #########  listbox entry
)
Recivers_name_entry_box.grid(row=2,column=0,padx=3,pady=1)

####################  buttons section frame  ########

Email_button_section_frame = Frame(
        Email_automate,
        
)
Email_button_section_frame.grid(row=0,column=1,padx=2,pady=2)

insert_delete_label_top = ttkb.Label(
        Email_button_section_frame,
        text="Insert/Delete",
        font=('carbel',8)                         #  top section of buttons label
        
)
insert_delete_label_top.pack(padx=3,pady=4)


#####  insert button

Insert_button_Email = ttkb.Button(
        Email_button_section_frame,
        text="Insert",
        width=12,
        command=Email_insert_btn
)
Insert_button_Email.pack(padx=3,pady=4)

###  delete button  top element

Delete_button_Email = ttkb.Button(
        Email_button_section_frame,
        text="Delete",
        width=12,
        command=Email_delete_btn
)
Delete_button_Email.pack(padx=3,pady=4)

#########  delete current selection button

delete_curr_button_Email = ttkb.Button(
        Email_button_section_frame,
        text="Delete sle",
        width=12,                    ### current select button
        command=Email_delete_curent_btn
)
delete_curr_button_Email.pack(padx=3,pady=4)

Label(Email_button_section_frame).pack(padx=3,pady=4)  ### empty label


###################################################################3


##################  email subject body frame

Email_sender_frame = Frame(
        Email_automate   ####  email body message frame
)
Email_sender_frame.grid(row=0,column=2,padx=2,pady=2,)

sender_mail_label = ttkb.Label(
            Email_sender_frame,
            text="sender mail",
            font=("arial",11),
            bootstyle="primarary"
            
)

sender_mail_label.grid(row=0,sticky=W,column=0)

email_sender_name = ttkb.Entry(
        Email_sender_frame,
        font=("arial",11),      #######    entry field of subject
        width=36,                                        #3 variable user name of sender
        bootstyle="info"
)
email_sender_name.grid(row=1,column=0,padx=2,pady=3)

sender_mail_password = ttkb.Label(
            Email_sender_frame,
            text="sender password",
            font=("arial",11),
            bootstyle="primarary"
            
)

sender_mail_password.grid(row=2,sticky=W,column=0,pady=2)

email_password_box = ttkb.Entry(
        Email_sender_frame,
        font=("arial",11),      #######    entry field of sender password
        width=36,
        bootstyle="info"
)
email_password_box.grid(row=3,column=0,padx=2,pady=3)

Email_message_body = ttkb.LabelFrame(
            Body_frame,
            text="Email message body",
            bootstyle="warning"
)

Email_message_body.grid(row=1,column=3,sticky=E,padx=6,pady=8,ipadx=5,ipady=3)
Email_message_body.pack_propagate(True)

subject_label_email = Label(
        Email_message_body,
        text="Subject",                 #####   subject 
        font=("arial",11),

)
subject_label_email.grid(row=0,column=0,sticky=W,padx=3,pady=4)


subject_label_email_box = ttkb.Entry(Email_message_body,
                                font=("arial",11),
                                width=31,
                                
                                )

                #### entry box of subject

subject_label_email_box.grid(row=1,column=0,sticky=W,padx=3,pady=4)

body_label_email = Label(
        Email_message_body,
        text="Body",                 #####   subject 
        font=("arial",11),

)
body_label_email.grid(row=2,sticky=W,column=0,padx=4,pady=2)

################  text area

body_text_eamil_area = Text(
        Email_message_body,
        width=38,height=9,
        wrap='word'
    )

body_text_eamil_area.grid(row=3,column=0,padx=3,pady=2)

Email_send_button = ttkb.Button(
        Email_message_body,
        text="send",
        bootstyle="info",
        width=27,
        command=Send_mail_smtp
)
Email_send_button.grid(row=4,column=0,padx=3,pady=2,sticky=W)



#########################################################################################################################################

###########  Auto typing

Auto_typing_body = ttkb.LabelFrame(
            Body_frame,
            text="AutoTyping",
            bootstyle="warning"
)

Auto_typing_body.grid(row=1,column=2,padx=6,pady=2,sticky=W,ipadx=5,ipady=3)
Auto_typing_body.pack_propagate(True)

########  text box

Text_area_label = Label(
        Auto_typing_body,
        text="Type text hear",
        font=('arial',12)
        
    )

Text_area_label.grid(row=0,column=0,padx=4,pady=5,sticky=W)

Text_area = Text(Auto_typing_body,
                 width=33,height=14,wrap="word")
Text_area.grid(row=1,column=0,padx=4,pady=5)     ############  main text area

Time_area = Label(
        Auto_typing_body,
        text="Time area",
        font=('arial',12)
        
    )
Time_area.grid(row=0,column=2,padx=4,pady=5)

time_area_delay_frame = Frame(Auto_typing_body)
time_area_delay_frame.grid(row=1,column=2,padx=4,pady=5)

Delay_time = Label(
        time_area_delay_frame,  #4#######  delay time label
        text="starts in",
        font=('ds-digital',12)
)
Delay_time.grid(row=0,column=0,padx=3,pady=4)

######     delay time entry box and button

####  delay time variable

strating_time_var = IntVar()
strating_time_var.set(7)

starting_time_box = ttkb.Entry(
        time_area_delay_frame,
        bootstyle="danger",
        width=13,
        textvariable=strating_time_var
)
starting_time_box.grid(row=1,column=0,padx=3,pady=4)

Label(time_area_delay_frame).grid(row=2,column=0,padx=3,pady=4)  ###@ blank label

#######   button

auto_tyle_btn = ttkb.Button(
        time_area_delay_frame,
        text="Type",
        bootstyle='info,outline',
        width=12,
        command=automatic_type
)
auto_tyle_btn.grid(row=3,column=0,padx=3,pady=4)


###############################################################################################################Bottom########################################################################################################################

###########  bottom side frame

Botton_Frame = ttkb.Frame(root,
           width=1540,height=73
           )

Botton_Frame.pack(side=BOTTOM,fill=X,pady=5)

Bottom_frame_Label = ttkb.LabelFrame(
            Botton_Frame,
            text="Google Youtube",
            bootstyle="primarary",
            width=1695,height=10
)
Bottom_frame_Label.pack_propagate(False)
Bottom_frame_Label.pack(side=LEFT,ipady=9,ipadx=11,pady=6,padx=12)

##########  Google search

Google_search = ttkb.Button(
        Bottom_frame_Label,text="Google",
        bootstyle="danger,outline",
        width=9,
        command=google_src
)
Google_search.grid(row=0,column=0,padx=13,pady=5)

Google_search_box = ttkb.Entry(
            Bottom_frame_Label,
            bootstyle='danger',
            font=('carbel',12),
            width=32,
)
Google_search_box.grid(row=0,column=1,padx=0,pady=5)

Label(Bottom_frame_Label,
      text="ㅤㅤㅤㅤㅤ"   ## blank text field
      ).grid(row=0,column=2) 

############   youtube search

youtube_search = ttkb.Button(
        Bottom_frame_Label,text="Youtybe",
        bootstyle="danger,outline",
        width=9,
        command=youtube_src
)
youtube_search.grid(row=0,column=3,padx=13,pady=5)

youtube_search_box = ttkb.Entry(
            Bottom_frame_Label,
            bootstyle='danger',
            font=('carbel',12),
            width=32,
)
youtube_search_box.grid(row=0,column=4,padx=0,pady=5)


################################################################################################################################################

################### 

##########  python modules 

Bottom_frame_Label2 = ttkb.LabelFrame(
            Botton_Frame,
            text="Install Module",
            bootstyle="primarary",
            width=369,height=19,
        
)
Bottom_frame_Label2.pack_propagate(False)
Bottom_frame_Label2.pack(side=RIGHT,ipady=9,ipadx=16,padx=22,)

#######  text 

Module_name = ttkb.Label(
        Bottom_frame_Label2,
        text="Module Name",
        bootstyle='success',
        font=('carbel',9),
)

Module_name.grid(row=0,column=0,padx=9,pady=5)

######  entry box
Module_variable = StringVar()

Module_box = ttkb.Entry(
            Bottom_frame_Label2,
            bootstyle='success',
            font=('carbel',12),
            width=20,
            textvariable=Module_variable
)
Module_box.grid(row=0,column=1,padx=2,pady=5)

Module_install_button = Ctk.CTkButton(
            Bottom_frame_Label2,
            text="Install",
            font=('carbel',19),
            width=28,command=Install_module
)

Module_install_button.grid(row=0,column=2,padx=16,ipadx=15,pady=5)


################  setting frame size

root.title("Auto🤖 Magic :~~ Nishant Maity")
root.geometry("1640x880")
root.maxsize(1640,880)
root.minsize(1640,880)
root.mainloop()