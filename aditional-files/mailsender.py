
import smtplib
import pyttsx3
sender = "nishantmaity7@gmail.com"
password = "nmbxyoucapoumxls"
reciver = ("nishantmaity096@gmail.com","uag","sharmilamaity3627@gmail.com")

subject = "how to creat dem"

body = """
When you connect a Windows 10 PC to the internet for the first 
prompt asks you to select   it is a win 
Lorem Ipsum adalah text contoh digunakan didalam industri pencetakan dan typesetting. Lorem Ipsum telah menjadi text contoh semenjak tahun ke 1500an, apabila pencetak yang kurang terkenal mengambil sebuah galeri cetak dan merobakanya menjadi satu buku spesimen. Ia telah bertahan bukan hanya selama lima kurun, tetapi telah melonjak ke era typesetting elektronik, dengan tiada perubahan ketara. Ia telah dipopularkan pada tahun 1960an dengan penerbitan Letraset yang mebawa kangungan Lorem Ipsum, dan lebih terkini dengan sofwer pencetakan desktop seperti Aldus PageMaker yang telah menyertakan satu versi Lorem Ipsum.
"""

message = f"""From:{sender}
To: {reciver}
subject: {subject}\n
{body}

"""

try:
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()

    server.login(sender,password)
    server.sendmail(sender,reciver,message)
    eng = pyttsx3.init()                 ## speak message
    eng.say(f"whatsapp Bomber has sent Messages")
    eng.runAndWait()

except:
    print("error...")
