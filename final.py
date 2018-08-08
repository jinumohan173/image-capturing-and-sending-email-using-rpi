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
	print "333"
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
	server.login(fromaddr, "way2jinu@gmail.com")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()
	print "888"

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while 1:
	 cam_on = GPIO.input(21)
	 if(cam_on==0):
		 print "111"
		 os.system ("sudo fswebcam -r 640x480 -s 15 image.jpg")
		 print "222"
		 with open("name.pdf","wb") as f1,open("/home/pi/image.jpg") as f2:
			 f1.write(img2pdf.convert(f2))
			 
		 mail_on()
			 
			 

