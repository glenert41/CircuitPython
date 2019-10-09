import simpleio
import pulseio
import time



class RGB:
    kind="colors"
    def __init__(self, r, g, b):


        self.pwm_r = pulseio.PWMOut(r, frequency=1000, duty_cycle=0)
        self.pwm_g = pulseio.PWMOut(g, frequency=1000, duty_cycle=0)  #sets the PWM pins
        self.pwm_b = pulseio.PWMOut(b, frequency=1000, duty_cycle=0)    

    def change_name(self, newName):
        self.name = newName

    def change_pins(self, r, g, b):
        self.r = r
        self.g = g    #Sets the input pins given to us by the main
        self.b = b

    def red(self):
        self.pwm_r.duty_cycle = 0
        self.pwm_g.duty_cycle = 2**16-1
        self.pwm_b.duty_cycle = 2**16-1


    def blue(self):
        self.pwm_r.duty_cycle = 2**16-1
        self.pwm_g.duty_cycle = 2**16-1
        self.pwm_b.duty_cycle = 0

    def magenta(self):
        self.pwm_r.duty_cycle = 0
        self.pwm_g.duty_cycle = 2**16-1
        self.pwm_b.duty_cycle = 0

    def green(self):
        self.pwm_r.duty_cycle = 2**16-1
        self.pwm_g.duty_cycle = 0
        self.pwm_b.duty_cycle = 2**16-1

    def cyan(self):
        self.pwm_r.duty_cycle = 2**16-1
        self.pwm_g.duty_cycle = 0
        self.pwm_b.duty_cycle = 0

    def yellow(self):
        self.pwm_r.duty_cycle = 0
        self.pwm_g.duty_cycle = 0
        self.pwm_b.duty_cycle = 2**16-1

    def rainbow(self, rate):



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







