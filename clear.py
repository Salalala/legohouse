import RPi.GPIO as GPIO
from time import *

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(10, GPIO.OUT)
GPIO.output(10, False)
GPIO.cleanup()




