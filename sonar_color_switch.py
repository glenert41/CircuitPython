#Graham Lenert
#CircuitPython Distance Sensor
#This assignment takes the distance from an UltraSonic Sensor,
    #and fades an LED throughout the rainbow to a corresponing color


import board
import neopixel
#import math
import time
#import digitalio
#import adafruit_bus_device
import adafruit_hcsr04
import simpleio

#sets up the distacne sensor (echo and trigger pin)
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D6, echo_pin=board.D5)
#simpleio.map_range(x, in_min, in_max, out_min, out_max)

#prepares the neopixel LED
dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness = .1)



r = 0
g = 0   #sets all the colors to 0
b = 0


while True:

    try: #attemps to run code
        print((sonar.distance,))
        if sonar.distance <= 20: #if the distance is less than 20

            r = simpleio.map_range(sonar.distance, 0,20,255,0)
            b = simpleio.map_range(sonar.distance, 5,20,0,255)
            g = simpleio.map_range(sonar.distance, 20,35,0,255)
        #maps the colors to their respective values

        else:
            r = simpleio.map_range(sonar.distance, 0,20,255,0)
            b = simpleio.map_range(sonar.distance, 35,20,0,255)
            g = simpleio.map_range(sonar.distance, 20,35,0,255)
        ##maps the colors to their respective values

        #fills the dot (changes the led color) to the RGB values
        dot.fill((int(r),int(g),int(b)))

    except RuntimeError: #If an error is return an error message (McDelivery)
        print("McDelivery")





    time.sleep(0.1)