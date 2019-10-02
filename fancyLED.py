import digitalio #pylint: disable-msg=import-error
import board #pylint: disable-msg=import-error
import time
import random

class FancyLED:

    def __init__(self, p1, p2, p3):

        self.p1 = digitalio.DigitalInOut(p1)
        self.p1.direction = digitalio.Direction.OUTPUT

        self.p2 = digitalio.DigitalInOut(p2)
        self.p2.direction = digitalio.Direction.OUTPUT

        self.p3 = digitalio.DigitalInOut(p3)
        self.p3.direction = digitalio.Direction.OUTPUT

    def alternate(self):

        self.p1.value = True
        self.p2.value = False
        self.p3.value = True
        time.sleep(.1)

        self.p1.value = False
        self.p2.value = True
        self.p3.value = False
        time.sleep(.1)


    def blink(self):

        self.p1.value = True
        self.p2.value = True
        self.p3.value = True
        time.sleep(0.1)
        self.p1.value = False
        self.p2.value = False
        self.p3.value = False
        time.sleep(0.1)


    def chase(self):
        self.p3.value = False
        self.p1.value = True
        time.sleep(0.1)
        self.p1.value = False
        self.p2.value = True
        time.sleep(0.1)
        self.p2.value = False
        self.p3.value = True
        time.sleep(0.1)

    def sparkle(self):


        n = random.randint(1,3)

        if n == 1:
            self.p1.value = True
            time.sleep(.5)
            self.p1.value = False
        elif n == 2:
            self.p2.value = True
            time.sleep(.5)
            self.p2.value = False
        elif n == 3:
            self.p3.value = True
            time.sleep(.5)
            self.p3.value = False

    def test(self):
        self.p2.value = True