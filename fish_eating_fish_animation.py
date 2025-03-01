import board
import pixelstrip
from colors import *

class FishAnimation(pixelstrip.Animation):
    """
    Write a description of this Animtion here.
    """
    def __init__(self, cycle_time=0.25):
        pixelstrip.Animation.__init__(self)
        self.cycle_time = cycle_time
        self.littlestep = 10
        self.bigstep = 0
        self.littlecycle = 0
        self.bigcycle = 0
        self.fish_color = [RED, BLUE, GREEN, YELLOW]
        self.bigcolor_cycle = 0
        self.littlecolor_cycle = 1
        self.bigcolorindex = 0
        self.littlecolorindex = 0
        self.littlefisheaten = False
        self.littlelifecycle = 0
    def reset(self, strip):
        self.timeout = self.cycle_time
        strip.clear()
        strip.show()
        # reset variables

    def draw(self, strip, delta_time):
        maxsteps = 32
        if self.bigstep >= maxsteps:
            self.bigstep = self.bigstep%maxsteps
            self.bigcycle = self.bigcycle + 1
            self.bigcolor_cycle = self.bigcycle%4
        if self.littlestep >= maxsteps:
            self.littlefisheaten = False
            self.littlestep = self.littlestep%maxsteps
            self.littlecycle = self.littlecycle + 1
            self.littlecolor_cycle = self.littlecycle%4
            self.littlelifecycle = self.littlelifecycle + 1
        if self.is_timed_out():
            if self.bigstep == self.littlestep:
                self.littlefisheaten = True
                self.littlelifecycle = -1
            if self.littlefisheaten == False:
                self.drawlittlefish(strip, maxsteps)
            self.drawlargefish(strip, maxsteps)        
            self.bigstep = self.bigstep+1
            if self.bigstep%2 == 0:
                self.littlestep = self.littlestep+1
            strip.show()
            self.timeout = self.cycle_time
    
    def drawlargefish(self, strip, maxsteps):        
        # change pixel values
        if self.bigstep%2 == 0:
            strip[self.bigstep*8+3] = self.fish_color[self.bigcolor_cycle]
            if self.bigstep<1:
                self.bigcolorindex = (self.bigcolor_cycle+3)%4
                start = (self.bigstep+maxsteps)*8 -5
            else:
                self.bigcolorindex = self.bigcolor_cycle
                start = (self.bigstep)*8 -5
            if self.bigcycle>0 or self.bigstep>= 1:
                for i in range(start, start+3):
                    strip[i] = self.fish_color[self.bigcolorindex]
            if self.bigstep<2:
                self.bigcolorindex = (self.bigcolor_cycle+3)%4
                start = (self.bigstep+maxsteps-1)*8 -7
            else:
                self.bigcolorindex = self.bigcolor_cycle
                start = (self.bigstep-1)*8 -7
            if self.bigcycle>0 or self.bigstep>= 2:
                for i in range(start, start+5):
                    strip[i] = self.fish_color[self.bigcolorindex]
            if self.bigstep<3:
                self.bigcolorindex = (self.bigcolor_cycle+3)%4
                start = (self.bigstep+maxsteps-2)*8 -6
            else:
                self.bigcolorindex = self.bigcolor_cycle
                start = (self.bigstep-2)*8 -6
            if self.bigcycle>0 or self.bigstep>= 3:
                for i in range(start, start+5):
                    strip[i] = self.fish_color[self.bigcolorindex]
            if self.bigstep<4:
                self.bigcolorindex = (self.bigcolor_cycle+3)%4
                start = (self.bigstep+maxsteps-3)*8 -8
            else:
                self.bigcolorindex = self.bigcolor_cycle
                start = (self.bigstep-3)*8 -8
            if self.bigcycle>0 or self.bigstep>= 4:
                for i in range(start, start+6):
                    strip[i] = self.fish_color[self.bigcolorindex]
            if self.bigstep<5:
                self.bigcolorindex = (self.bigcolor_cycle+3)%4
                start = (self.bigstep+maxsteps-4)*8 -7
            else:
                self.bigcolorindex = self.bigcolor_cycle
                start = (self.bigstep-4)*8 -7
            if self.bigcycle>0 or self.bigstep>= 5:
                for i in range(start, start+6):
                    strip[i] = self.fish_color[self.bigcolorindex]
            if self.bigstep<6:
                self.bigcolorindex = (self.bigcolor_cycle+3)%4
                start = (self.bigstep+maxsteps-5)*8 -7
            else:
                self.bigcolorindex = self.bigcolor_cycle
                start = (self.bigstep-5)*8 -7
            if self.bigcycle>0 or self.bigstep>= 6:
                for i in range(start, start+5):
                    strip[i] = self.fish_color[self.bigcolorindex]
            if self.bigstep<7:
                self.bigcolorindex = (self.bigcolor_cycle+3)%4
                start = (self.bigstep+maxsteps-6)*8 -5
            else:
                self.bigcolorindex = self.bigcolor_cycle
                start = (self.bigstep-6)*8 -5
            if self.bigcycle>0 or self.bigstep>= 7:
                for i in range(start, start+3):
                    strip[i] = self.fish_color[self.bigcolorindex]
            if self.bigstep<8:
                self.bigcolorindex = (self.bigcolor_cycle+3)%4
                start = (self.bigstep+maxsteps-7)*8 -7
            else:
                self.bigcolorindex = self.bigcolor_cycle
                start = (self.bigstep-7)*8 -7
            if self.bigcycle>0 or self.bigstep>= 8:
                for i in range(start, start+5):
                    strip[i] = self.fish_color[self.bigcolorindex]
            if self.bigstep<9:
                self.bigcolorindex = (self.bigcolor_cycle+3)%4
                start = (self.bigstep+maxsteps-8)*8 -7
            else:
                self.bigcolorindex = self.bigcolor_cycle
                start = (self.bigstep-8)*8 -7
            if self.bigcycle>0 or self.bigstep>= 9:
                for i in range(start, start+7):
                    strip[i] = self.fish_color[self.bigcolorindex]
                
            strip[((self.bigstep-8)*8 +0 +maxsteps*8)%(maxsteps*8)] = BLACK
            strip[((self.bigstep-8)*8 +6 +maxsteps*8)%(maxsteps*8)] = BLACK
            strip[((self.bigstep-7)*8 +1 +maxsteps*8)%(maxsteps*8)] = BLACK
            strip[((self.bigstep-7)*8 +2 +maxsteps*8)%(maxsteps*8)] = BLACK
            strip[((self.bigstep-7)*8 +6 +maxsteps*8)%(maxsteps*8)] = BLACK
            strip[((self.bigstep-7)*8 +7 +maxsteps*8)%(maxsteps*8)] = BLACK
            strip[((self.bigstep-6)*8 +0 +maxsteps*8)%(maxsteps*8)] = BLACK
            strip[((self.bigstep-6)*8 +6 +maxsteps*8)%(maxsteps*8)] = BLACK
            strip[((self.bigstep-5)*8 +7 +maxsteps*8)%(maxsteps*8)] = BLACK

        else:
            strip[self.bigstep*8+4] = self.fish_color[self.bigcolor_cycle]
            if self.bigstep<1:
                self.bigcolorindex = (self.bigcolor_cycle+3)%4
                start = (self.bigstep+maxsteps)*8 -6
            else:
                self.bigcolorindex = self.bigcolor_cycle
                start = (self.bigstep)*8 -6
            if self.bigcycle>0 or self.bigstep>= 1:
                for i in range(start, start+3):
                    strip[i] = self.fish_color[self.bigcolorindex]
            if self.bigstep<2:
                self.bigcolorindex = (self.bigcolor_cycle+3)%4
                start = (self.bigstep+maxsteps-1)*8 -6
            else:
                self.bigcolorindex = self.bigcolor_cycle
                start = (self.bigstep-1)*8 -6
            if self.bigcycle>0 or self.bigstep>= 2:
                for i in range(start, start+5):
                    strip[i] = self.fish_color[self.bigcolorindex]
            if self.bigstep<3:
                self.bigcolorindex = (self.bigcolor_cycle+3)%4
                start = (self.bigstep+maxsteps-2)*8 -7
            else:
                self.bigcolorindex = self.bigcolor_cycle
                start = (self.bigstep-2)*8 -7
            if self.bigcycle>0 or self.bigstep>= 3:
                for i in range(start, start+5):
                    strip[i] = self.fish_color[self.bigcolorindex]
            if self.bigstep<4:
                self.bigcolorindex = (self.bigcolor_cycle+3)%4
                start = (self.bigstep+maxsteps-3)*8 -6
            else:
                self.bigcolorindex = self.bigcolor_cycle
                start = (self.bigstep-3)*8 -6
            if self.bigcycle>0 or self.bigstep>= 4:
                for i in range(start, start+6):
                    strip[i] = self.fish_color[self.bigcolorindex]
            if self.bigstep<5:
                self.bigcolorindex = (self.bigcolor_cycle+3)%4
                start = (self.bigstep+maxsteps-4)*8 -7
            else:
                self.bigcolorindex = self.bigcolor_cycle
                start = (self.bigstep-4)*8 -7
            if self.bigcycle>0 or self.bigstep>= 5:
                for i in range(start, start+6):
                    strip[i] = self.fish_color[self.bigcolorindex]
            if self.bigstep<6:
                self.bigcolorindex = (self.bigcolor_cycle+3)%4
                start = (self.bigstep+maxsteps-5)*8 -6
            else:
                self.bigcolorindex = self.bigcolor_cycle
                start = (self.bigstep-5)*8 -6
            if self.bigcycle>0 or self.bigstep>= 6:
                for i in range(start, start+5):
                    strip[i] = self.fish_color[self.bigcolorindex]
            if self.bigstep<7:
                self.bigcolorindex = (self.bigcolor_cycle+3)%4
                start = (self.bigstep+maxsteps-6)*8 -6
            else:
                self.bigcolorindex = self.bigcolor_cycle
                start = (self.bigstep-6)*8 -6
            if self.bigcycle>0 or self.bigstep>= 7:
                for i in range(start, start+3):
                    strip[i] = self.fish_color[self.bigcolorindex]
            if self.bigstep<8:
                self.bigcolorindex = (self.bigcolor_cycle+3)%4
                start = (self.bigstep+maxsteps-7)*8 -6
            else:
                self.bigcolorindex = self.bigcolor_cycle
                start = (self.bigstep-7)*8 -6
            if self.bigcycle>0 or self.bigstep>= 8:
                for i in range(start, start+5):
                    strip[i] = self.fish_color[self.bigcolorindex]
            if self.bigstep<9:
                self.bigcolorindex = (self.bigcolor_cycle+3)%4
                start = (self.bigstep+maxsteps-8)*8 -8
            else:
                self.bigcolorindex = self.bigcolor_cycle
                start = (self.bigstep-8)*8 -8
            if self.bigcycle>0 or self.bigstep>= 9:
                for i in range(start, start+7):
                    strip[i] = self.fish_color[self.bigcolorindex]
            strip[((self.bigstep-8)*8 +1 +maxsteps*8)%(maxsteps*8)] = BLACK
            strip[((self.bigstep-8)*8 +7 +maxsteps*8)%(maxsteps*8)] = BLACK
            strip[((self.bigstep-7)*8 +0 +maxsteps*8)%(maxsteps*8)] = BLACK
            strip[((self.bigstep-7)*8 +1 +maxsteps*8)%(maxsteps*8)] = BLACK
            strip[((self.bigstep-7)*8 +5 +maxsteps*8)%(maxsteps*8)] = BLACK
            strip[((self.bigstep-7)*8 +6 +maxsteps*8)%(maxsteps*8)] = BLACK
            strip[((self.bigstep-6)*8 +1 +maxsteps*8)%(maxsteps*8)] = BLACK
            strip[((self.bigstep-6)*8 +7 +maxsteps*8)%(maxsteps*8)] = BLACK
            strip[((self.bigstep-5)*8 +0 +maxsteps*8)%(maxsteps*8)] = BLACK
        if self.bigstep<10:
            start = int((self.bigstep+maxsteps-10)*8)
        else:
            start = int((self.bigstep-10)*8)
        for i in range(start, start+8):
            strip[i] = BLACK

    def drawlittlefish(self, strip, maxsteps):
        # change pixel values
        if self.littlestep%2 == 0:
            strip[self.littlestep*8+3] = self.fish_color[self.littlecolor_cycle]
            if self.littlestep<1:
                self.littlecolorindex = (self.littlecolor_cycle+3)%4
                start = (self.littlestep+maxsteps)*8 -5
            else:
                self.littlecolorindex = self.littlecolor_cycle
                start = (self.littlestep)*8 -5
            if self.littlelifecycle>0 or self.littlestep>= 1:
                for i in range(start, start+3):
                    strip[i] = self.fish_color[self.littlecolorindex]
            if self.littlestep<2:
                self.littlecolorindex = (self.littlecolor_cycle+3)%4
                start = (self.littlestep+maxsteps-1)*8 -7
            else:
                self.littlecolorindex = self.littlecolor_cycle
                start = (self.littlestep-1)*8 -7
            if self.littlelifecycle>0 or self.littlestep>= 2:
                for i in range(start, start+5):
                    strip[i] = self.fish_color[self.littlecolorindex]
            if self.littlestep<3:
                self.littlecolorindex = (self.littlecolor_cycle+3)%4
                start = (self.littlestep+maxsteps-2)*8 -6
            else:
                self.littlecolorindex = self.littlecolor_cycle
                start = (self.littlestep-2)*8 -6
            if self.littlelifecycle>0 or self.littlestep>= 3:
                for i in range(start, start+5):
                    strip[i] = self.fish_color[self.littlecolorindex]
            if self.littlestep<4:
                self.littlecolorindex = (self.littlecolor_cycle+3)%4
                start = (self.littlestep+maxsteps-3)*8 -6
            else:
                self.littlecolorindex = self.littlecolor_cycle
                start = (self.littlestep-3)*8 -6
            if self.littlelifecycle>0 or self.littlestep>= 4:
                for i in range(start, start+3):
                    strip[i] = self.fish_color[self.littlecolorindex]
            if self.littlestep<5:
                self.littlecolorindex = (self.littlecolor_cycle+3)%4
                start = (self.littlestep+maxsteps-4)*8-6
            else:
                self.littlecolorindex = self.littlecolor_cycle
                start = (self.littlestep-4)*8 -6
            if self.littlelifecycle>0 or self.littlestep>= 5:
                for i in range(start, start+5):
                    strip[i] = self.fish_color[self.littlecolorindex]
            strip[((self.littlestep-3)*8 -7 +maxsteps*8)%(maxsteps*8)] = BLACK
            strip[((self.littlestep-3)*8 -3 +maxsteps*8)%(maxsteps*8)] = BLACK

        else:
            strip[self.littlestep*8+4] = self.fish_color[self.littlecolor_cycle]
            if self.littlestep<1:
                self.littlecolorindex = (self.littlecolor_cycle+3)%4
                start = (self.littlestep+maxsteps)*8 -6
            else:
                self.littlecolorindex = self.littlecolor_cycle
                start = (self.littlestep)*8 -6
            if self.littlelifecycle>0 or self.littlestep>= 1:
                for i in range(start, start+3):
                    strip[i] = self.fish_color[self.littlecolorindex]
            if self.littlestep<2:
                self.littlecolorindex = (self.littlecolor_cycle+3)%4
                start = (self.littlestep+maxsteps-1)*8 -6
            else:
                self.littlecolorindex = self.littlecolor_cycle
                start = (self.littlestep-1)*8 -6
            if self.littlelifecycle>0 or self.littlestep>= 2:
                for i in range(start, start+5):
                    strip[i] = self.fish_color[self.littlecolorindex]
            if self.littlestep<3:
                self.littlecolorindex = (self.littlecolor_cycle+3)%4
                start = (self.littlestep+maxsteps-2)*8 -7
            else:
                self.littlecolorindex = self.littlecolor_cycle
                start = (self.littlestep-2)*8 -7
            if self.littlelifecycle>0 or self.littlestep>= 3:
                for i in range(start, start+5):
                    strip[i] = self.fish_color[self.littlecolorindex]
            if self.littlestep<4:
                self.littlecolorindex = (self.littlecolor_cycle+3)%4
                start = (self.littlestep+maxsteps-3)*8 -5
            else:
                self.littlecolorindex = self.littlecolor_cycle
                start = (self.littlestep-3)*8 -5
            if self.littlelifecycle>0 or self.littlestep>= 4:
                for i in range(start, start+3):
                    strip[i] = self.fish_color[self.littlecolorindex]
            if self.littlestep<5:
                self.littlecolorindex = (self.littlecolor_cycle+3)%4
                start = (self.littlestep+maxsteps-4)*8 -7
            else:
                self.littlecolorindex = self.littlecolor_cycle
                start = (self.littlestep-4)*8 -7
            if self.littlelifecycle>0 or self.littlestep>= 5:
                for i in range(start, start+5):
                    strip[i] = self.fish_color[self.littlecolorindex]
            strip[((self.littlestep-3)*8 -6 +maxsteps*8)%(maxsteps*8)] = BLACK
            strip[((self.littlestep-3)*8 -2 +maxsteps*8)%(maxsteps*8)] = BLACK
        if self.littlestep<6:
            start = int((self.littlestep+maxsteps-6)*8)
        else:
            start = int((self.littlestep-6)*8)

        for i in range(start, start+8):
            strip[i] = BLACK

if __name__ == "__main__":
    strip_gp15 = pixelstrip.PixelStrip(board.GP15, width=32, height=8, bpp=4, pixel_order=pixelstrip.GRB, options={pixelstrip.MATRIX_COLUMN_MAJOR, pixelstrip.MATRIX_ZIGZAG})
    strip_gp15.animation = FishAnimation()      
    while True:
        strip_gp15.draw()
