import board
import pixelstrip
from colors import *

# This is a a minimal example of an Animation.
# All Animations must define a draw().  It's also a good
# idea to define an __init__ function for initializing the 
# Animation and a reset function to reset things every time
# the Animation restarts.

class WaveAnimation(pixelstrip.Animation):
    """
    Write a description of this Animtion here.
    """
    def __init__(self, cycle_time=0.005):
        pixelstrip.Animation.__init__(self)
        self.cycle_time = cycle_time
        # variable setup
        self.step = 0
        self.cycle = 0

    def reset(self, strip):
        self.timeout = self.cycle_time
        strip.clear()
        strip.show()
        # reset variables

    def draw(self, strip, delta_time):
        length = 144
        if self.is_timed_out():
            # change pixel value
            if self.cycle == 0: 
                strip[self.step] = PURPLE
            else:
                strip[self.step] = BLACK
            self.step = self.step + 1
            if self.step == length:
                self.cycle = 1-self.cycle
                self.step = 0
            strip.show()
            self.timeout = self.cycle_time


if __name__ == "__main__":
    strip_gp15 = pixelstrip.PixelStrip(board.GP15, width=32, height=8, bpp=4, pixel_order=pixelstrip.GRB, options={pixelstrip.MATRIX_COLUMN_MAJOR, pixelstrip.MATRIX_ZIGZAG})
    strip_gp15.animation = WaveAnimation()
    while True:
        strip_gp15.draw()
