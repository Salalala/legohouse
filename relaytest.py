import RPi.GPIO as GPIO
from time import *

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

while(True):
	relay_pin1 = 8
	relay_pin2 = 10
	GPIO.setup(relay_pin1, GPIO.OUT)
	GPIO.setup(relay_pin2, GPIO.OUT)
	GPIO.output(relay_pin1, False)
	GPIO.output(relay_pin2, True)
	sleep(2)
	GPIO.output(relay_pin1, True)
	GPIO.output(relay_pin2, False)
	sleep(2)
