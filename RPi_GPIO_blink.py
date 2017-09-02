import sys
import os
import tkinter
import random
import time
import RPi.GPIO as GPIO
#tells the pi to set pin 7 as an output
GPIO.setup(7, GPIO.OUT)

GPIO.setmode(GPIO.BOARD)
# Makes it blink from 0 to 3 times
for x in range(0, 3): 
    GPIO.output(7, True) # Turns the 7th switch on
    time.sleep(1)
    GPIO.output(7, False) # Turns the 7th switch off
    time.sleep(1)
GPIO.cleanup() #Sets the GPIO back to nuetral

