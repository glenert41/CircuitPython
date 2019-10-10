#Graham Lenert
#Photointerrupter
#This code takes a photorupters interruptions over the course of 4 seconds, 
    # and prints the amount of interruptions



import board
#import neopixel
import math
import time
import digitalio
import adafruit_bus_device

#^ Imports Libraries

photoPin = digitalio.DigitalInOut(board.D8)
photoPin.direction = digitalio.Direction.INPUT
photoPin.pull = digitalio.Pull.UP
#Sets the Photointerrupter Pin as an Input and Digital Pin 8


initial = time.monotonic()   #Starts Timer 

interrupts = -1         
lread = True
fread = True   #Sets the fread and lread variables to True


while True:
    now = time.monotonic() 
    if now - initial == 4: #if it has been 4 seconds
        print("Number of interruptions: " + str(interrupts))
        initial = time.monotonic()

    if photoPin.value:
        lread = True   #if interrupted, turn lread to true

    elif fread == lread: #if the photointerrupter is interrupted, then uniterrupted,
                                #count the interrupter and add 1 to the counter variable
        interrupts +=1   
        lread = not lread

