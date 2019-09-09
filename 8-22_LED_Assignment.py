#Graham Lenert
#LED Fade
#This makes an LED Fade in and out

import board
import neopixel
import math
import time
import digitalio
import analogio

led = analogio.AnalogOut(board.A0) #sets the A0 pin as an analog Output

holder = 0               #this is the value that the LED is associated with
changer = 3000           #This is the value that the LED changes by

while True:
    led.value = holder     #Sets the LED to a value
    time.sleep(0.1)
    holder += changer      #adds brightness (or subtracts)
    print(holder)          #prints to serial monitor


    if holder >= 60000:
        changer *= -1       #if the led is at the threshold, it makes the changer negative

    if holder <= 2000:
        changer *= -1

















