#Graham Lenert
#Photointerrupter
#This code takes a photorupters interruptions over the course of 4 seconds, and prints the amount of interruptions



import board
#import neopixel
import math
import time
import digitalio
import adafruit_bus_device

photoPin = digitalio.DigitalInOut(board.D8)
photoPin.direction = digitalio.Direction.INPUT
photoPin.pull = digitalio.Pull.UP

initial = time.monotonic()

interrupts = -1
lread = True
fread = True


while True:
    now = time.monotonic()
    if now - initial == 4:
        print("Number of interruptions: " + str(interrupts))
        initial = time.monotonic()

    if photoPin.value:
        lread = True

    elif fread == lread:
        interrupts +=1
        lread = not lread

