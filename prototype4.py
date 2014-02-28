#!/usr/bin/env python

from random import *
from time import *

import RPi.GPIO as GPIO, time, os
import os

from logToDb import initConn as initConn
from logToDb import logAlarm as logAlarm
from dbMapper import getIdFromLastPicture as getIdFromLastPicture
from dbMapper import logPhoto as logPhoto

from matrix_keypad import RPi_GPIO
kp = RPi_GPIO.keypad(columnCount = 3)


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

codeToActivate = 111

def init():
	GPIO.setmode(GPIO.BOARD)
	global pressureListener_pin
	global led_pin
	global doorListener_pin
	global motor_pin
	pressureListener_pin = 8
	led_pin = 5
	doorListener_pin = 13
	motor_pin = 10
	GPIO.setup(led_pin, GPIO.OUT)
	GPIO.setup(pressureListener_pin, GPIO.IN)
	GPIO.setup(doorListener_pin, GPIO.IN)
	GPIO.setup(motor_pin, GPIO.OUT)


def securitySystem():
	if(activateAlarm()):
		print("Alarm activated")
		init()
		while True:		
			print("Secure")
			if(GPIO.input(pressureListener_pin) == False):
				pressurePlateSequence()
			if(GPIO.input(doorListener_pin) == False):
				doorSequence()		
			if(RCtime(18) > 400):
				safeSequence()                				

def activateAlarm():
	kp = RPi_GPIO.keypad(columnCount = 3)
	print "Please enter a 3 digit code: "
	code = ""
	digit = ""
	
	for i in xrange(0,3):
		digit = getDigit()
		print digit
		time.sleep(0.2)
		code += str(digit)
	if(str(code) == str(codeToActivate)):
		return True
	else:
		return False

def safeSequence():
	cur, conn = initConn()
	print("Someone opened the safe, logging to db, sending notification...")
	logAlarm(cur, conn, "The safe just opened!")
	notify("Someone opened the safe", "2")
	playAlarm()
	GPIO.output(motor_pin, True)
	sleep(2)
	GPIO.output(motor_pin, False)


def notify(notification, priority):
	os.system('perl nma.pl -apikeyfile=apikey -application="%s" -event="%s" -notification="%s" -priority=-2' % ("Legohouse", notification, priority) ) 	
	

def pressurePlateSequence():
	cur, conn = initConn()
	print("Someone on pressure plate, logging to db, photo uploading...")
	logAlarm(cur, conn, "Someone on pressure plate, photo uploading...")
	takePicture()
	
def getDigit():
	r = None
	while r == None:
		r = kp.getKey()
	return r
	
def takePicture():
	cur, con = initConn()
	id = getIdFromLastPicture(cur, con)
	idFromNextPicture = int(id) + 1
	imageName = "image" + str(idFromNextPicture) + ".jpg"
	imagePath = "/etc/scripts/img/" + imageName
	os.system('raspistill -o "%s" -w 200 -h 150' % (imagePath) )
	remotehost = '193.191.187.55'
	remotefile = '/var/www/img/'+ imageName
	os.system('scp "%s" "%s:%s"' % (imagePath, remotehost, remotefile) )
	cur, con = initConn()
	logPhoto(cur, con, idFromNextPicture)

def doorSequence():
	cur, conn = initConn()
	logAlarm(cur, conn, 'Door opened while alarm is active')	
	print("Intruder detected, door opened")
	playAlarm()
        
     
def RCtime(RCpin):
	reading = 0
    	GPIO.setup(RCpin, GPIO.OUT)
    	GPIO.output(RCpin, GPIO.LOW)
    	time.sleep(0.1)
     
    	GPIO.setup(RCpin, GPIO.IN)
    	# This takes about 1 millisecond per loop cycle
    	while (GPIO.input(RCpin) == GPIO.LOW):
    		reading += 1
    	return reading


def playAlarm():
	os.system('mpg321 /etc/scripts/sounds/alarm1.mp3')
	GPIO.output(led_pin, False)
	time.sleep(0.5)
	GPIO.output(led_pin, True)
     
securitySystem()
