from random import *
from time import *
from sendmail import *
import RPi.GPIO as GPIO
button_pin = 7
led_pin = 5
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN)
GPIO.setwarnings(False)

while True:
	if(GPIO.input(button_pin)==False):
		print("THE BUTTON WORKS LEL")
		GPIO.output(led_pin, True);
		sleep(0.4)
		sendmail()
		GPIO.output(led_pin, False);
		
