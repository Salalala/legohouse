from random import *
from time import *
#from ledscript import *
import RPi.GPIO as GPIO
import os
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

def prototype1():
	button_pin = 7
	led_pin = 5
	GPIO.setup(led_pin, GPIO.OUT)
	GPIO.setup(button_pin, GPIO.IN)
	

	while True:
		if(GPIO.input(button_pin)==False):
			for x in range(0, 20):
				print("THE BUTTON WORKS LEL")
				os.system('mpg321 /etc/scripts/sounds/alarm1.mp3')
				GPIO.output(led_pin, False);
				sleep(0.4)
				GPIO.output(led_pin, True);
		

prototype1()
