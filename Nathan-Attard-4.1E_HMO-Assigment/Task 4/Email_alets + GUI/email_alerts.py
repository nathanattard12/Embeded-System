import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# set up the SMTP server
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'nathanattard12345@gmail.com'
sender_password = 'oidkjaqhrkvkuopd'
receiver_email = 'nathanattard12345@gmail.com'

# create message object
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = 'Python email alert'
body = 'This is an email alert from Python '
message.attach(MIMEText(body, 'plain'))

# send the message
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(sender_email, sender_password)
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)

