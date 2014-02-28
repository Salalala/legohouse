#!/usr/bin/env python
     
# Example for RC timing reading for Raspberry Pi
# Must be used with GPIO 0.3.1a or later - earlier verions
# are not fast enough!
    
import RPi.GPIO as GPIO, time, os
    

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
     
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
     
while True:
	if (RCtime(18) < 1000):
		print("De safe just opened, release the cows!")
		print("Mooh")    	
		print RCtime(18)
