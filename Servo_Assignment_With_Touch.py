#Graham Lenert
#Servo Control
#This assignment makes a servo turn when a wire is touched, 
    # and turns it another way when another wire is touched

import board
import digitalio
import analogio
import time             #importing libraries
import simpleio
import pulseio
from adafruit_motor import servo
import touchio


#sets the PWM pin for servo
pwm = pulseio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency=50)
touch_A1 = touchio.TouchIn(board.A1)  #activates the touch wires
touch_A2 = touchio.TouchIn(board.A2)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm) q   #sets the servo pin to the pwm pin
servo_angle = 0   #starts servo at 0

while True:
    #if wire 1 touched, turn servo
    if touch_A1.value and servo_angle < 180:
        print("touched a1")
        servo_angle += 5
        my_servo.angle = servo_angle

    #if wire 2 touched, turn servo
    if touch_A2.value and servo_angle > 0:
        print("touched a2")
        servo_angle -= 5
        my_servo.angle = servo_angle

    time.sleep(0.01) #sleep for execution safety