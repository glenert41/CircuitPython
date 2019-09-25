from rgb import RGB   # import the RGB class from the rgb module
import board
import time

r1 = board.D1
g1 = board.D2
b1 = board.D3

r2 = board.D4
g2 = board.D5
b2 = board.D7

rate1 = 0.01
rate2 = 0.001

myRGB1 = RGB(r1,g1,b1)   # create a new RGB object, using pins 2, 3, and 4
myRGB2 = RGB(r2,g2,b2)   # create a new RGB object, using pins 5, 6, and 7

myRGB1.change_pins(r1,g1,b1)
print(myRGB1.kind)
#print(myRGB2.kind)
myRGB1.change_name("rex")
print(myRGB1.name)



myRGB1.red()          # Glow red
myRGB2.green()        # Glow green
time.sleep(1)
myRGB1.blue()         # Glow blue
myRGB2.cyan()         # Glow... you get it...
time.sleep(1)
myRGB1.magenta()      # Did you know magenta isn't in the rainbow?
myRGB2.yellow()       # Like you learned in first grade, red and green make... huh?
time.sleep(1)
# extra spicy (optional) part
myRGB1.rainbow(rate1) # Fade through the colors of the rainbow at the given rate.  Oooooh, pretty!
myRGB2.rainbow(rate2) # Fade through the colors of the rainbow at the given rate.  Oooooh, pretty!
#time