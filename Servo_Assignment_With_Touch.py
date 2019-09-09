
import board
import neopixel
#import math
import time
#import digitalio
#import adafruit_bus_device
import adafruit_hcsr04
import simpleio

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D6, echo_pin=board.D5)
#simpleio.map_range(x, in_min, in_max, out_min, out_max)

dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness = .1)



r = 0
g = 0
b = 0


while True:

    try:
        print((sonar.distance,))
        if sonar.distance <= 20:

            r = simpleio.map_range(sonar.distance, 0,20,255,0)
            b = simpleio.map_range(sonar.distance, 5,20,0,255)
            g = simpleio.map_range(sonar.distance, 20,35,0,255)

        else:
            r = simpleio.map_range(sonar.distance, 0,20,255,0)
            b = simpleio.map_range(sonar.distance, 35,20,0,255)
            g = simpleio.map_range(sonar.distance, 20,35,0,255)

        dot.fill((int(r),int(g),int(b)))
    except RuntimeError:
        print("McDelivery")





    time.sleep(0.1)