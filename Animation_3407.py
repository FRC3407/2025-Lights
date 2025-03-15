import board
import pixelstrip
import bmp

# Animation to display a list of bitmap files.

class Team3407Animation(pixelstrip.Animation):
    def __init__(self, file_names, cycle_time=1.0, flip=None):
        pixelstrip.Animation.__init__(self)
        self.cycle_time = cycle_time
        self.file_names = file_names
        self.bitmaps = []
        for name in file_names:
            self.bitmaps.append(bmp.BmpFile(name))
        self.frame = 0
        if flip is not None:
            self.flip = flip
        else:
            self.flip = self.bitmaps[0].biXPelsPerMeter > 0

    def reset(self, strip):
        strip.clear()
        strip.show()
        self.frame = 0
        self.timeout = 0.0

    def draw(self, strip, delta_time):
        if self.is_timed_out():
            self.display_bitmap(strip, self.bitmaps[self.frame])
            strip.show()
            self.frame = (self.frame + 1) % len(self.bitmaps)
            self.timeout = self.cycle_time
    
    def display_bitmap(self, strip, bitmap):
        for y in range(strip.height):
            if y < bitmap.height:
                for x in range(strip.width):
                    if x < bitmap.width:
                        yy = y if not self.flip else strip.height-(y+1)
                        strip[x, yy] = bitmap[x, y]
                

if __name__ == "__main__":
    matrix = pixelstrip.PixelStrip(board.GP15, width=32, height=8, bpp=4, pixel_order=pixelstrip.GRB, options={pixelstrip.MATRIX_COLUMN_MAJOR, pixelstrip.MATRIX_ZIGZAG})
    matrix.animation = Team3407Animation(['3407.bmp'])
    while True:
        matrix.draw()
    