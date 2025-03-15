import board
import pixelstrip
from colors import *

# This is a a minimal example of an Animation.
# All Animations must define a draw().  It's also a good
# idea to define an __init__ function for initializing the 
# Animation and a reset function to reset things every time
# the Animation restarts.

class CircleAnimation(pixelstrip.Animation):
    """
    Write a description of this Animtion here.
    """
    def __init__(self, cycle_time=0.05):
        pixelstrip.Animation.__init__(self)
        self.cycle_time = cycle_time
        self.step = 0
        # variable setup

    def reset(self, strip):
        self.timeout = self.cycle_time
        strip.clear()
        strip.show()
        # reset variables

    def draw(self, strip, delta_time):
        strip_length = 24
        if self.is_timed_out():
            # change pixel values
            next1 = (self.step+1)%strip_length
            next2 = (self.step+9)%strip_length
            next3 = (self.step+17)%strip_length
            previous1 = (self.step+strip_length-1)%strip_length
            previous2 = (self.step+strip_length+7)%strip_length
            previous3 = (self.step+strip_length+15)%strip_length
            strip[next1] = AQUA
            strip[next2] = AQUA
            strip[next3] = AQUA
            strip[previous1] = BLACK
            strip[previous2] = BLACK
            strip[previous3] = BLACK
            strip.show()
            self.step = (self.step+1)%strip_length
            self.timeout = self.cycle_time


if __name__ == "__main__":
    strip_gp15 = pixelstrip.PixelStrip(board.GP15, 24, bpp=4, pixel_order=pixelstrip.GRB)
    strip_gp15.animation = CircleAnimation