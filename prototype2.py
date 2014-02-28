from random import *
from time import *
import RPi.GPIO as GPIO
import os
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pressureListener_pin = 7
led_pin = 5
magnet_pin = 16
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(pressureListener_pin, GPIO.IN)
GPIO.setup(magnet_pin, GPIO.IN)

def securitySystem():
	while True:
		print("secure")
		if(GPIO.input(pressureListener_pin) == GPIO.HIGH):
			alarmPressurePlate()
		if(GPIO.input(magnet_pin) == False):
			alarmMagnet()		
		

def alarmPressurePlate():	
	print("Someone on pressure plate")
	sleep(0.5)
	print("-")
	os.system('mpg321 /etc/scripts/sounds/alarm1.mp3')
        GPIO.output(led_pin, False);
        sleep(0.4)
        GPIO.output(led_pin, True);

def alarmMagnet():	
	print("Intruder detected")
	sleep(0.5)
	print("-")
	os.system('mpg321 /etc/scripts/sounds/alarm1.mp3')
        GPIO.output(led_pin, False);
        sleep(0.4)
        GPIO.output(led_pin, True);


securitySystem()

