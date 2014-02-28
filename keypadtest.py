from matrix_keypad import RPi_GPIO
from time import sleep
import RPi.GPIO as GPIO 


# Initialize the keypad class
kp = RPi_GPIO.keypad(columnCount = 3)
GPIO.setwarnings(False) 



def digit():
    # Loop while waiting for a keypress
    r = None
    while r == None:
        r = kp.getKey()
    return r 
 

def enterCode():
	print "Please enter a 4 digit code: "
	code = "" 
	cijfer = 0
	for i in xrange(0,4):
		cijfer = digit()
		print cijfer
		sleep(0.2)
		code += str(cijfer)
	 
		# d2 = digit()
		# print d2
		# sleep(1)
	 
		# d3 = digit()
		# print d3
		# sleep(0.2)
	 
		# d4 = digit()
		# sleep(0.2)
		# print d4
	print code
	return code

enterCode()
