from random import *
from time import *
import RPi.GPIO as GPIO
import os
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
magnet_pin = 12
GPIO.setup(magnet_pin, GPIO.OUT)
GPIO.output(magnet_pin, False)

def magnet():
	
	
	GPIO.setup(magnet_pin, GPIO.IN)
	 

	while True:
		if(GPIO.input(magnet_pin) == False):
			print("Intruder detected")
			sleep(0.5)
			print("-")
magnet()
