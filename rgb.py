#Graham Lenert
#september 2019
#This code is the library for the RGB color changer. 
# The assignment is the Classes, Objects, and Modules in canvas. 
    #It sets an LED to the color that you call, and also has a rainbow function.
    #Only works when you set 3 pins in the main



import simpleio
import pulseio
import time



class RGB:                  #creates the class
    kind="colors"
    def __init__(self, r, g, b):

        #sets the entered pins to PWM pins
        self.pwm_r = pulseio.PWMOut(r, frequency=1000, duty_cycle=0)
        self.pwm_g = pulseio.PWMOut(g, frequency=1000, duty_cycle=0)  #sets the PWM pins
        self.pwm_b = pulseio.PWMOut(b, frequency=1000, duty_cycle=0)    

    def change_pins(self, r, g, b):
        self.r = r
        self.g = g    #Sets the input pins given to us by the main
        self.b = b

    def red(self):              #turns on red
        self.pwm_r.duty_cycle = 0
        self.pwm_g.duty_cycle = 2**16-1
        self.pwm_b.duty_cycle = 2**16-1


    def blue(self):             #turns on blue
        self.pwm_r.duty_cycle = 2**16-1
        self.pwm_g.duty_cycle = 2**16-1
        self.pwm_b.duty_cycle = 0

    def magenta(self):          #turns on magenta (red and blue)
        self.pwm_r.duty_cycle = 0
        self.pwm_g.duty_cycle = 2**16-1
        self.pwm_b.duty_cycle = 0

    def green(self):            #turns on green
        self.pwm_r.duty_cycle = 2**16-1
        self.pwm_g.duty_cycle = 0
        self.pwm_b.duty_cycle = 2**16-1

    def cyan(self):             #turns on cyan (green and blue)
        self.pwm_r.duty_cycle = 2**16-1
        self.pwm_g.duty_cycle = 0
        self.pwm_b.duty_cycle = 0

    def yellow(self):           #turns on yellow (green and red)
        self.pwm_r.duty_cycle = 0
        self.pwm_g.duty_cycle = 0
        self.pwm_b.duty_cycle = 2**16-1

    def rainbow(self, rate):
            #rate is the delay (how fast the LED color changes)

            #fades through the rainbow
        for val in range(0,2**16,128):
            self.pwm_r.duty_cycle = 0
            self.pwm_g.duty_cycle = 2**16-1 - val
            self.pwm_b.duty_cycle = 2**16-1
            time.sleep(rate)
        for val in range(0,2**16,128):
            self.pwm_r.duty_cycle = 2**16-1
            self.pwm_g.duty_cycle = val
            self.pwm_b.duty_cycle = 2**16-1 - val
            time.sleep(rate)
        for val in range(0,2**16,128):
            self.pwm_r.duty_cycle = 2**16-1 - val
            self.pwm_g.duty_cycle = 2**16-1
            self.pwm_b.duty_cycle = val
            time.sleep(rate)







