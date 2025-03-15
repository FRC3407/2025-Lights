import board
import pixelstrip
from colors import *

class Flashing_Green_Animation(pixelstrip.Animation):
    """
    Write a description of this Animtion here.
    """
    def __init__(self, cycle_time=0.5):
        pixelstrip.Animation.__init__(self)
        self.cycle_time = cycle_time
        # variable setup
        self.w = 8
        self.l = 32
        self.c = 0

    def reset(self, strip):
        self.timeout = self.cycle_time
        strip.clear()
        strip.show()
        # reset variables

    def draw(self, strip, delta_time):
        if self.is_timed_out():
            # change pixel values
            if self.c == 0:
                for i in range(0, self.w*self.l):
                    strip[i] = GREEN
            else:
                for i in range(0, self.w*self.l):
                    strip[i] = BLACK
            self.c = 1 - self.c
            strip.show()
            self.timeout = self.cycle_time


if __name__ == "__main__":
    strip_gp15 = pixelstrip.PixelStrip(board.GP15, width=32, height=8, bpp=4, pixel_order=pixelstrip.GRB, options={pixelstrip.MATRIX_COLUMN_MAJOR, pixelstrip.MATRIX_ZIGZAG})
    strip_gp15.animation = Flashing_Green_Animation()
    while True:
        strip_gp15.draw()