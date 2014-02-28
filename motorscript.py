from random import *
from time import *
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
motor_pin = 10
GPIO.setup(motor_pin, GPIO.OUT)



while True:
	
	GPIO.output(motor_pin, 1)
	sleep(2)
	GPIO.output(motor_pin, 0)
	sleep(2)
