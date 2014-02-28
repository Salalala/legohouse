import RPi.GPIO as GPIO
from time import *

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)



def blink(led):
	led_pin = led;
	GPIO.setup(led_pin, GPIO.OUT)
	while True:
		GPIO.output(led_pin, True)
		sleep(0.1)
		GPIO.output(led_pin, False)
		sleep(0.1)
        	GPIO.output(led_pin, True)
        	sleep(0.1)
        	GPIO.output(led_pin, False)
        	sleep(0.1)
        	GPIO.output(led_pin, True)
        	sleep(0.1)
        	GPIO.output(led_pin, False)
        	sleep(0.1)
		GPIO.output(led_pin, True)
		sleep(1)
		GPIO.output(led_pin, False)
		sleep(0.1)
		GPIO.output(led_pin, True)
		sleep(1)
		GPIO.output(led_pin, False)
		sleep(1)
		#GPIO.cleanup()

led = raw_input("What output pin are you going to use? ")
blink(int(led))
