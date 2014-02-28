#!/usr/bin/env python


from random import *
from time import *
from matrix_keypad import RPi_GPIO
import RPi.GPIO as GPIO, time, os
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Keypad
kp = RPi_GPIO.keypad(columnCount = 3)
GPIO.setwarnings(False)

#Listeners for door, pressure plate, motor and led
pressureListener_pin = 8
led_pin = 5
doorListener_pin = 13
motor_pin = 10

GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(pressureListener_pin, GPIO.IN)
GPIO.setup(doorListener_pin, GPIO.IN)
GPIO.setup(motor_pin, GPIO.OUT)


def readKey():
	r = None
	while r == None:
		r = kp.getKey()
	return r

def enterCode():
	print "Please enter a 3 digit code to activate the alarm: "
	code = ""
	digit = ""
	for i in xrange(0,3):
		digit = readKey()
		print digit
		sleep(0.2)
		code += str(digit)
	print code
	return code

def securitySystem():
	while True:		
		print("secure")
		#if(GPIO.input(pressureListener_pin) == False):
		#	alarmPressurePlate()
		if(GPIO.input(doorListener_pin) == False):
			alarmDoor()		
		if(RCtime(18) > 1000):
			print("The safe just opened, release the cows!")
                	print("Mooh")
                			

def alarmPressurePlate():	
	print("Someone on pressure plate")
	sleep(0.5)
	print("-")
	os.system('mpg321 /etc/scripts/sounds/alarm1.mp3')
        GPIO.output(led_pin, False)
        sleep(0.5)
        GPIO.output(led_pin, True)
	GPIO.output(motor_pin, True)
	sleep(2)
	GPIO.output(motor_pin, False)

def alarmDoor():	
	print("Intruder detected")
	sleep(0.5)
	print("-")
	os.system('mpg321 /etc/scripts/sounds/alarm1.mp3')
        GPIO.output(led_pin, False)
        sleep(0.5)
        GPIO.output(led_pin, True)
     
def RCtime (RCpin):
	reading = 0
    	GPIO.setup(RCpin, GPIO.OUT)
    	GPIO.output(RCpin, GPIO.LOW)
    	time.sleep(0.1)
     
    	GPIO.setup(RCpin, GPIO.IN)
    	# This takes about 1 millisecond per loop cycle
    	while (GPIO.input(RCpin) == GPIO.LOW):
    		reading += 1
    	return reading
     

#code = enterCode()
#if (code == "23*"):
#	securitySystem()

securitySystem()
