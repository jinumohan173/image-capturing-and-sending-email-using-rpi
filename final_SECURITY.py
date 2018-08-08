# AUTHOR :- jinu.m
#DOC :-  13/07/2017
#TOC:-14:00


import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
import os
import time
import img2pdf
import RPi.GPIO as GPIO

def mail_on():
	print "sending mail"
	fromaddr = "jinumohan173@gmail.com"
	toaddr = "way2jinu@gmail.com"
 
	msg = MIMEMultipart()
 
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "Security alert"
 
	body = "hi, its email from rpi the captured image "
 
	msg.attach(MIMEText(body, 'plain'))
 
	filename = ".pdf"
	attachment = open("/home/pi/name.pdf", "rb")
 
	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
	msg.attach(part)
 
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "type ur email password")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()
	print "process over check your email"
	return 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)

while 1:
	
	 GPIO.output(20,0)
	 GPIO.output(16,0)
	 cam_on = GPIO.input(21)
	 if(cam_on==0):
		 GPIO.output(20,1)
		 print "image capturing"
		 os.system ("sudo fswebcam -r 640x480 -s 15 image.jpg")
		 print "image captured "
		 with open("name.pdf","wb") as f1,open("/home/pi/image.jpg") as f2:
			 f1.write(img2pdf.convert(f2))
			 
		 mail_on()
		 GPIO.output(20,1)
		 GPIO.output(16,1)
		 time.sleep(7)
		 cam_on=1
			 
			 

