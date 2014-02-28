from random import *
from time import *
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
listen_pin = 12
motor_pin = 10
GPIO.setmode(GPIO.BOARD)


GPIO.setup(motor_pin, GPIO.OUT)
GPIO.setup(listen_pin, GPIO.IN)

while True:
	if(GPIO.input(listen_pin)==True):
		print("button pushed")		
		GPIO.output(motor_pin, True)
	
		
