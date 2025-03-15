import board
import pixelstrip
from colors import *

# This is a a minimal example of an Animation.
# All Animations must define a draw().  It's also a good
# idea to define an __init__ function for initializing the 
# Animation and a reset function to reset things every time
# the Animation restarts.

class CelebrationAnimation(pixelstrip.Animation):
    """
    Write a description of this Animtion here.
    """
    def __init__(self, cycle_time=0.2):
        pixelstrip.Animation.__init__(self)
        self.cycle_time = cycle_time
        self.cycle = 0
        self.wave = 0
        self.wavecolor = [WHITE, TURQUOISE, AQUA, BLUEVIOLET, MIDNIGHTBLUE, DARKBLUE]
        # variable setup
        #GREEN POSIBLITY GREENYELLOW, GREEN, FORESTGREEN

    def reset(self, strip):
        self.timeout = self.cycle_time
        strip.clear()
        strip.show()
        # reset variables

    def draw(self, strip, delta_time):
        striplength = 144
        wavegap = 6
        maxwaves = int(striplength/wavegap/2)
        if self.is_timed_out():
            # change pixel value
            for i in range(0, maxwaves+1):
                cycle = int(self.cycle-(i*wavegap)+int(striplength/2))%int(striplength/2)
                colorindex = i%6
                self.explosion(strip, striplength, cycle, colorindex)
            self.cycle = (self.cycle + 1)%int(striplength/2)
            if self.cycle%wavegap == 0:
                self.wave = (self.wave+1)%maxwaves
            strip.show()
            self.timeout = self.cycle_time

    def explosion(self, strip, striplength, cycle, colorindex):
        strip[int(striplength/2)-cycle] = self.wavecolor[colorindex]
        strip[int(striplength/2)+cycle] = self.wavecolor[colorindex]
        if cycle == 0:
            strip[1] = BLACK
            strip[striplength-1] = BLACK
        else:
            strip[int(striplength/2)-cycle+1] = BLACK
            strip[int(striplength/2)+cycle-1] = BLACK

if __name__ == "__main__":
    strip_gp15 = pixelstrip.PixelStrip(board.GP15, width=32, height=8, bpp=4, pixel_order=pixelstrip.GRB, options={pixelstrip.MATRIX_COLUMN_MAJOR, pixelstrip.MATRIX_ZIGZAG})
    strip_gp15.animation = CelebrationAnimation()
    while True:
        strip_gp15.draw()
