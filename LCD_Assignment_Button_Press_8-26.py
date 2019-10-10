#Graham Lenert
#LCD Assignment Button Press
#This assignment; when you press a button, the counter goes up or down
    #on the LCD screen depending on which way a switch is flipped

#LCD Screen

import board
#import neopixel
import math
import time
import digitalio
import adafruit_bus_device

from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface #importing and prepping LCD library

from lcd.lcd import CursorMode

lcd = LCD(I2CPCF8574Interface(0x3f), num_rows=2, num_cols=16)
#^ defines the dimensions of the LCD screen

#sets pin 7 to an input
inputPin = digitalio.DigitalInOut(board.D7)
inputPin.direction = digitalio.Direction.INPUT
inputPin.pull = digitalio.Pull.UP 


#Sets the pin 8 to an Input
button = digitalio.DigitalInOut(board.D8)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

counter = 0 #sets counter to 0
oldSwitchState = 0 #States the Old State to 0 (Switch starts off)
newSwitchState = 1 #States the New State to 1(Updating switch starts on)
adder = 1
while True:

    lcd.clear()
    lcd.set_cursor_pos(0,0)         #clears and resets LCD
    lcd.print("Presses: ")     # Sets the amount of Button Presses

    lcd.set_cursor_pos(1,0)
    lcd.print(str(counter))

    if button.value:
        print("0")
        time.sleep(0.05)
        oldSwitchState = 0


    elif oldSwitchState == 0 and newSwitchState == 1:
        if inputPin.value:
            adder = 1
        else:
            adder = -1              
        #Only Prints when Button is Pressed then Released    
        print("1")
        #print(str(adder))
        time.sleep(0.05)
        counter += adder
        oldSwitchState = 1
        #Resets The Variables (Sets the Button to Unpressed)