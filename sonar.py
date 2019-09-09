
import board
import neopixel
import math
import time
import digitalio
import adafruit_bus_device
import adafruit_hcsr04
import simpleio

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D6, echo_pin=board.D5)
#simpleio.map_range(x, in_min, in_max, out_min, out_max)

led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.3

while True:

    dot.fill((int(r),int(g),int(b)))
    '''
    try:
        print((sonar.distance,))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)'''