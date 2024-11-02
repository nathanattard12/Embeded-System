import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, render_template
from datetime import datetime
import os
import time

#import RPi.GPIO as GPIO
#from rpi_lcd import LCD
import threading	


app = Flask(__name__)



smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'nathanattard12345@gmail.com'
sender_password = 'oidkjaqhrkvkuopd'
receiver_email = 'nathanattard12345@gmail.com'


def send_email():
	"""Ths will send an email displaying the temperature """
	message = MIMEMultipart()
	message['From'] = sender_email
	message['To'] = receiver_email
	message['Subject'] = 'Python email alert'
	body = 'Tempreture = ' + str(read_temp()) 
	message.attach(MIMEText(body, 'plain'))
	with smtplib.SMTP(smtp_server, smtp_port) as server:
		server.starttls()
		server.login(sender_email, sender_password)
		text = message.as_string()
		server.sendmail(sender_email, receiver_email, text)
	
#lcd= LCD()

#temp_sensor = '/sys/bus/w1/devices/10-00080232f3ad/w1_slave'

#def setup():
#    os.system('modprobe w1-gpio')
#    os.system('modprobe w1-therm')
#    GPIO.setwarnings(False)

#def temp_raw():
#    f = open(temp_sensor,'r')
#    lines = f.readlines()
#    f.close()
#    return lines

#def read_temp():
#    lines = temp_raw()
#    while lines[0].strip()[-3:] != 'YES':
#        time.sleep(0.2)
#        lines = temp_raw()

#    temp_output = lines[1].find('t=')

#    if temp_output != -1:
#        temp_string = lines[1].strip()[temp_output + 2:]
#        temp_c = float(temp_string)/1000
#        return round(temp_c,1)

#def destroy():
#	print("Cleaning up ...")
#	GPIO.cleanup()
#	lcd.clear()

#def lcd_temp():	
#	"""Thiss will keep updating the temperature to the LCD and te time every time"""
#	while True:
#		temp = read_temp()
#		lcd.text("Temp:" + str(temp) + "C",2)
#		lcd.text(time.strftime("%H:%M"),1)


@app.route('/')
def home():
	while True:
		date = datetime.now().strftime("%A %d %B %Y")
#		temp = read_temp()
		return render_template('index.html', date=date)
			 #, temp=temp)


@app.route('/send_email', methods=['POST'])
def send_email_route():
	send_email()
	return "Email was send  !!!!"


#try:
#	setup()
#	lcd_thread = threading.Thread(target=lcd_temp)
#	lcd_thread.start()	
app.run()	
#except KeyboardInterrupt:
#	lcd.clear()
#	destroy()
