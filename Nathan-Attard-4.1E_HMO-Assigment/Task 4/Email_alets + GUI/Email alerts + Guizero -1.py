from guizero import *
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'nathanattard12345@gmail.com'
sender_password = 'oidkjaqhrkvkuopd'
receiver_email = 'nathanattard12345@gmail.com'

def send_email():

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = 'Python email alert'
    body = 'This is an email alert from Python'
    message.attach(MIMEText(body, 'plain'))


    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)

def update_time():
    date_now = datetime.datetime.today()
    formatted_date = date_now.strftime("%A, %d %B %Y, %H:%M:%S")
    date.value = formatted_date
    date.after(1000, update_time)


app = App(title="Weather Station", bg="blue")

text = Text(app, text="Weather for today", font="Helvetica", size=30, color="white", width=80, height=2, bg="darkcyan")


email_button = PushButton(app, text="Send email", width=500, height=2, command=send_email)
email_button.bg ="gray"
email_button.text_color = "white"

date = Text(app, text="", bg="black", width=100, height=1, color="white", size=25)

Temp = Text(app, text="Temperature\n\n25C", width=70, height=10, bg="cyan", align="left")



update_time()

date.tk.pack(padx=0,pady=10)
Temp.tk.pack(padx=10, pady=10)

app.display()
