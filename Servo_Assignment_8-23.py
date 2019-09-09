

import board
import neopixel
import math
import time
import digitalio
import analogio
import pulseio
from adafruit_motor import servo
import touchio

touch_A1 = touchio.TouchIn(board.A1)
touch_A2 = touchio.TouchIn(board.A2)


# create a PWMOut object on Pin A2.
pwm = pulseio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:

if touch_A1.value:
    print('a1 touched')

   ''' for i in range (1, 180, 1):
        time.sleep(0.01)
        print(i)
        my_servo.angle = i


    for i in range (180, 1, -1):
        time.sleep(0.01)
        print(i)
        my_servo.angle = i
'''

    #my_servo.angle = angle
time.sleep(1)











