import board
import pixelstrip
from colors import *

class LittleFishAnimation(pixelstrip.Animation):
    """
    Write a description of this Animtion here.
    """
    def __init__(self, cycle_time=0.4):
        pixelstrip.Animation.__init__(self)
        self.cycle_time = cycle_time
        self.step = 0
        self.cycle = 0
        self.fish_color = [RED, BLUE, GREEN, YELLOW]
        self.color_cycle = 0
    def reset(self, strip):
        self.timeout = self.cycle_time
        strip.clear()
        strip.show()
        # reset variables

    def draw(self, strip, delta_time):
        maxsteps = 32
        color_index = 0
        if self.step >= maxsteps:
            self.step = self.step%maxsteps
            self.cycle = self.cycle + 1
            self.color_cycle = self.cycle%4
        if self.is_timed_out():
            # change pixel values
            if self.step%2 == 0:
                strip[self.step*8+3] = self.fish_color[self.color_cycle]
                if self.step<1:
                    color_index = (self.color_cycle+3)%4
                    start = (self.step+maxsteps)*8 -5
                else:
                    color_index = self.color_cycle
                    start = (self.step)*8 -5
                if self.cycle>0 or self.step>= 1:
                    for i in range(start, start+3):
                        strip[i] = self.fish_color[color_index]
                if self.step<2:
                    color_index = (self.color_cycle+3)%4
                    start = (self.step+maxsteps-1)*8 -7
                else:
                    color_index = self.color_cycle
                    start = (self.step-1)*8 -7
                if self.cycle>0 or self.step>= 2:
                    for i in range(start, start+5):
                        strip[i] = self.fish_color[color_index]
                if self.step<3:
                    color_index = (self.color_cycle+3)%4
                    start = (self.step+maxsteps-2)*8 -6
                else:
                    color_index = self.color_cycle
                    start = (self.step-2)*8 -6
                if self.cycle>0 or self.step>= 3:
                    for i in range(start, start+5):
                        strip[i] = self.fish_color[color_index]
                if self.step<4:
                    color_index = (self.color_cycle+3)%4
                    start = (self.step+maxsteps-3)*8 -6
                else:
                    color_index = self.color_cycle
                    start = (self.step-3)*8 -6
                if self.cycle>0 or self.step>= 4:
                    for i in range(start, start+3):
                        strip[i] = self.fish_color[color_index]
                if self.step<5:
                    color_index = (self.color_cycle+3)%4
                    start = (self.step+maxsteps-4)*8-6
                else:
                    color_index = self.color_cycle
                    start = (self.step-4)*8 -6
                if self.cycle>0 or self.step>= 5:
                    for i in range(start, start+5):
                        strip[i] = self.fish_color[color_index]
                strip[((self.step-3)*8 -7 +maxsteps*8)%(maxsteps*8)] = BLACK
                strip[((self.step-3)*8 -3 +maxsteps*8)%(maxsteps*8)] = BLACK

            else:
                strip[self.step*8+4] = self.fish_color[self.color_cycle]
                if self.step<1:
                    color_index = (self.color_cycle+3)%4
                    start = (self.step+maxsteps)*8 -6
                else:
                    color_index = self.color_cycle
                    start = (self.step)*8 -6
                if self.cycle>0 or self.step>= 1:
                    for i in range(start, start+3):
                        strip[i] = self.fish_color[color_index]
                if self.step<2:
                    color_index = (self.color_cycle+3)%4
                    start = (self.step+maxsteps-1)*8 -6
                else:
                    color_index = self.color_cycle
                    start = (self.step-1)*8 -6
                if self.cycle>0 or self.step>= 2:
                    for i in range(start, start+5):
                        strip[i] = self.fish_color[color_index]
                if self.step<3:
                    color_index = (self.color_cycle+3)%4
                    start = (self.step+maxsteps-2)*8 -7
                else:
                    color_index = self.color_cycle
                    start = (self.step-2)*8 -7
                if self.cycle>0 or self.step>= 3:
                    for i in range(start, start+5):
                        strip[i] = self.fish_color[color_index]
                if self.step<4:
                    color_index = (self.color_cycle+3)%4
                    start = (self.step+maxsteps-3)*8 -5
                else:
                    color_index = self.color_cycle
                    start = (self.step-3)*8 -5
                if self.cycle>0 or self.step>= 4:
                    for i in range(start, start+3):
                        strip[i] = self.fish_color[color_index]
                if self.step<5:
                    color_index = (self.color_cycle+3)%4
                    start = (self.step+maxsteps-4)*8 -7
                else:
                    color_index = self.color_cycle
                    start = (self.step-4)*8 -7
                if self.cycle>0 or self.step>= 5:
                    for i in range(start, start+5):
                        strip[i] = self.fish_color[color_index]
                strip[((self.step-3)*8 -6 +maxsteps*8)%(maxsteps*8)] = BLACK
                strip[((self.step-3)*8 -2 +maxsteps*8)%(maxsteps*8)] = BLACK
            if self.step<6:
                start = int((self.step+maxsteps-6)*8)
            else:
                start = int((self.step-6)*8)

            for i in range(start, start+8):
                strip[i] = BLACK
                    
            self.step = self.step+1
            strip.show()
            self.timeout = self.cycle_time

class BigFishAnimation(pixelstrip.Animation):
    """
    Write a description of this Animtion here.
    """
    def __init__(self, cycle_time=0.5):
        pixelstrip.Animation.__init__(self)
        self.cycle_time = cycle_time
        self.step = 0
        self.cycle = 0
        self.fish_color = [RED, BLUE, GREEN, YELLOW]
        self.color_cycle = 0
    def reset(self, strip):
        self.timeout = self.cycle_time
        strip.clear()
        strip.show()
        # reset variables

    def draw(self, strip, delta_time):
        maxsteps = 32
        color_index = 0
        if self.step >= maxsteps:
            self.step = self.step%maxsteps
            self.cycle = self.cycle + 1
            self.color_cycle = self.cycle%4
        if self.is_timed_out():
            # change pixel values
            if self.step%2 == 0:
                strip[self.step*8+3] = self.fish_color[self.color_cycle]
                if self.step<1:
                    color_index = (self.color_cycle+3)%4
                    start = (self.step+maxsteps)*8 -5
                else:
                    color_index = self.color_cycle
                    start = (self.step)*8 -5
                if self.cycle>0 or self.step>= 1:
                    for i in range(start, start+3):
                        strip[i] = self.fish_color[color_index]
                if self.step<2:
                    color_index = (self.color_cycle+3)%4
                    start = (self.step+maxsteps-1)*8 -7
                else:
                    color_index = self.color_cycle
                    start = (self.step-1)*8 -7
                if self.cycle>0 or self.step>= 2:
                    for i in range(start, start+5):
                        strip[i] = self.fish_color[color_index]
                if self.step<3:
                    color_index = (self.color_cycle+3)%4
                    start = (self.step+maxsteps-2)*8 -6
                else:
                    color_index = self.color_cycle
                    start = (self.step-2)*8 -6
                if self.cycle>0 or self.step>= 3:
                    for i in range(start, start+5):
                        strip[i] = self.fish_color[color_index]
                if self.step<4:
                    color_index = (self.color_cycle+3)%4
                    start = (self.step+maxsteps-3)*8 -8
                else:
                    color_index = self.color_cycle
                    start = (self.step-3)*8 -8
                if self.cycle>0 or self.step>= 4:
                    for i in range(start, start+6):
                        strip[i] = self.fish_color[color_index]
                if self.step<5:
                    color_index = (self.color_cycle+3)%4
                    start = (self.step+maxsteps-4)*8 -7
                else:
                    color_index = self.color_cycle
                    start = (self.step-4)*8 -7
                if self.cycle>0 or self.step>= 5:
                    for i in range(start, start+6):
                        strip[i] = self.fish_color[color_index]
                if self.step<6:
                    color_index = (self.color_cycle+3)%4
                    start = (self.step+maxsteps-5)*8 -7
                else:
                    color_index = self.color_cycle
                    start = (self.step-5)*8 -7
                if self.cycle>0 or self.step>= 6:
                    for i in range(start, start+5):
                        strip[i] = self.fish_color[color_index]
                if self.step<7:
                    color_index = (self.color_cycle+3)%4
                    start = (self.step+maxsteps-6)*8 -5
                else:
                    color_index = self.color_cycle
                    start = (self.step-6)*8 -5
                if self.cycle>0 or self.step>= 7:
                    for i in range(start, start+3):
                        strip[i] = self.fish_color[color_index]
                if self.step<8:
                    color_index = (self.color_cycle+3)%4
                    start = (self.step+maxsteps-7)*8 -7
                else:
                    color_index = self.color_cycle
                    start = (self.step-7)*8 -7
                if self.cycle>0 or self.step>= 8:
                    for i in range(start, start+5):
                        strip[i] = self.fish_color[color_index]
                if self.step<9:
                    color_index = (self.color_cycle+3)%4
                    start = (self.step+maxsteps-8)*8 -7
                else:
                    color_index = self.color_cycle
                    start = (self.step-8)*8 -7
                if self.cycle>0 or self.step>= 9:
                    for i in range(start, start+7):
                        strip[i] = self.fish_color[color_index]
                    
                strip[((self.step-8)*8 +0 +maxsteps*8)%(maxsteps*8)] = BLACK
                strip[((self.step-8)*8 +6 +maxsteps*8)%(maxsteps*8)] = BLACK
                strip[((self.step-7)*8 +1 +maxsteps*8)%(maxsteps*8)] = BLACK
                strip[((self.step-7)*8 +2 +maxsteps*8)%(maxsteps*8)] = BLACK
                strip[((self.step-7)*8 +6 +maxsteps*8)%(maxsteps*8)] = BLACK
                strip[((self.step-7)*8 +7 +maxsteps*8)%(maxsteps*8)] = BLACK
                strip[((self.step-6)*8 +0 +maxsteps*8)%(maxsteps*8)] = BLACK
                strip[((self.step-6)*8 +6 +maxsteps*8)%(maxsteps*8)] = BLACK
                strip[((self.step-5)*8 +7 +maxsteps*8)%(maxsteps*8)] = BLACK

            else:
                strip[self.step*8+4] = self.fish_color[self.color_cycle]
                if self.step<1:
                    color_index = (self.color_cycle+3)%4
                    start = (self.step+maxsteps)*8 -6
                else:
                    color_index = self.color_cycle
                    start = (self.step)*8 -6
                if self.cycle>0 or self.step>= 1:
                    for i in range(start, start+3):
                        strip[i] = self.fish_color[color_index]
                if self.step<2:
                    color_index = (self.color_cycle+3)%4
                    start = (self.step+maxsteps-1)*8 -6
                else:
                    color_index = self.color_cycle
                    start = (self.step-1)*8 -6
                if self.cycle>0 or self.step>= 2:
                    for i in range(start, start+5):
                        strip[i] = self.fish_color[color_index]
                if self.step<3:
                    color_index = (self.color_cycle+3)%4
                    start = (self.step+maxsteps-2)*8 -7
                else:
                    color_index = self.color_cycle
                    start = (self.step-2)*8 -7
                if self.cycle>0 or self.step>= 3:
                    for i in range(start, start+5):
                        strip[i] = self.fish_color[color_index]
                if self.step<4:
                    color_index = (self.color_cycle+3)%4
                    start = (self.step+maxsteps-3)*8 -6
                else:
                    color_index = self.color_cycle
                    start = (self.step-3)*8 -6
                if self.cycle>0 or self.step>= 4:
                    for i in range(start, start+6):
                        strip[i] = self.fish_color[color_index]
                if self.step<5:
                    color_index = (self.color_cycle+3)%4
                    start = (self.step+maxsteps-4)*8 -7
                else:
                    color_index = self.color_cycle
                    start = (self.step-4)*8 -7
                if self.cycle>0 or self.step>= 5:
                    for i in range(start, start+6):
                        strip[i] = self.fish_color[color_index]
                if self.step<6:
                    color_index = (self.color_cycle+3)%4
                    start = (self.step+maxsteps-5)*8 -6
                else:
                    color_index = self.color_cycle
                    start = (self.step-5)*8 -6
                if self.cycle>0 or self.step>= 6:
                    for i in range(start, start+5):
                        strip[i] = self.fish_color[color_index]
                if self.step<7:
                    color_index = (self.color_cycle+3)%4
                    start = (self.step+maxsteps-6)*8 -6
                else:
                    color_index = self.color_cycle
                    start = (self.step-6)*8 -6
                if self.cycle>0 or self.step>= 7:
                    for i in range(start, start+3):
                        strip[i] = self.fish_color[color_index]
                if self.step<8:
                    color_index = (self.color_cycle+3)%4
                    start = (self.step+maxsteps-7)*8 -6
                else:
                    color_index = self.color_cycle
                    start = (self.step-7)*8 -6
                if self.cycle>0 or self.step>= 8:
                    for i in range(start, start+5):
                        strip[i] = self.fish_color[color_index]
                if self.step<9:
                    color_index = (self.color_cycle+3)%4
                    start = (self.step+maxsteps-8)*8 -8
                else:
                    color_index = self.color_cycle
                    start = (self.step-8)*8 -8
                if self.cycle>0 or self.step>= 9:
                    for i in range(start, start+7):
                        strip[i] = self.fish_color[color_index]
                strip[((self.step-8)*8 +1 +maxsteps*8)%(maxsteps*8)] = BLACK
                strip[((self.step-8)*8 +7 +maxsteps*8)%(maxsteps*8)] = BLACK
                strip[((self.step-7)*8 +0 +maxsteps*8)%(maxsteps*8)] = BLACK
                strip[((self.step-7)*8 +1 +maxsteps*8)%(maxsteps*8)] = BLACK
                strip[((self.step-7)*8 +5 +maxsteps*8)%(maxsteps*8)] = BLACK
                strip[((self.step-7)*8 +6 +maxsteps*8)%(maxsteps*8)] = BLACK
                strip[((self.step-6)*8 +1 +maxsteps*8)%(maxsteps*8)] = BLACK
                strip[((self.step-6)*8 +7 +maxsteps*8)%(maxsteps*8)] = BLACK
                strip[((self.step-5)*8 +0 +maxsteps*8)%(maxsteps*8)] = BLACK
            if self.step<10:
                start = int((self.step+maxsteps-10)*8)
            else:
                start = int((self.step-10)*8)
            for i in range(start, start+8):
                strip[i] = BLACK
                    
            self.step = self.step+1
            strip.show()
            self.timeout = self.cycle_time

if __name__ == "__main__":
    strip_gp15 = pixelstrip.PixelStrip(board.GP15, width=32, height=8, bpp=4, pixel_order=pixelstrip.GRB, options={pixelstrip.MATRIX_COLUMN_MAJOR, pixelstrip.MATRIX_ZIGZAG})
    strip_gp15.animation = LittleFishAnimation()
    strip_gp14 = pixelstrip.PixelStrip(board.GP14, width=32, height=8, bpp=4, pixel_order=pixelstrip.GRB, options={pixelstrip.MATRIX_COLUMN_MAJOR, pixelstrip.MATRIX_ZIGZAG})
    strip_gp14.animation = BigFishAnimation()      
    while True:
        strip_gp15.draw()
        strip_gp14.draw()
