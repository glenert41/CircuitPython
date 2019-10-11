#Graham Lenert
#FancyLED
#In this assignment, we set out a grouping of 6 LEDS, and wrote functions to make cool patterns and visuals.



import digitalio #pylint: disable-msg=import-error
import board #pylint: disable-msg=import-error
import time  #imports time
import random #imports random

class FancyLED:

    def __init__(self, p1, p2, p3):

        self.p1 = digitalio.DigitalInOut(p1)            #sets the pin fed by the user to pin 1 to an output
        self.p1.direction = digitalio.Direction.OUTPUT

        self.p2 = digitalio.DigitalInOut(p2)         #sets the pin fed by the user to pin 2 to an output
        self.p2.direction = digitalio.Direction.OUTPUT

        self.p3 = digitalio.DigitalInOut(p3)         #sets the pin fed by the user to pin 3 to an output
        self.p3.direction = digitalio.Direction.OUTPUT

    def alternate(self):

        self.p1.value = True
        self.p2.value = False      #turns on the first set
        self.p3.value = True       
        time.sleep(.1)

        self.p1.value = False
        self.p2.value = True        #turns on the second set
        self.p3.value = False
        time.sleep(.1)


    def blink(self):

        self.p1.value = True
        self.p2.value = True        #turns all LEDs on
        self.p3.value = True
        time.sleep(0.1)
        self.p1.value = False
        self.p2.value = False       #turns all LEDs off
        self.p3.value = False
        time.sleep(0.1)


    def chase(self):
        self.p3.value = False
        self.p1.value = True
        time.sleep(0.1)
        self.p1.value = False       #chasing pattern for the LEDs
        self.p2.value = True
        time.sleep(0.1)
        self.p2.value = False
        self.p3.value = True
        time.sleep(0.1)

    def sparkle(self):


        n = random.randint(1,3)     #randomly selects a number between 1 and 3

        if n == 1:
            self.p1.value = True        #turns LED on if random number is 1
            time.sleep(.5)
            self.p1.value = False
        elif n == 2:                    #turns LED on if random number is 2
            self.p2.value = True
            time.sleep(.5)
            self.p2.value = False
        elif n == 3:                    #turns LED on if random number is 3
            self.p3.value = True
            time.sleep(.5)
            self.p3.value = False

    def test(self):                     #troubleshooting LEDS
        self.p2.value = True
        