import board
import pixelstrip
from colors import *
import math

def transform_matrix(x,y):
    return [
        [1,0,x],
        [0,1,y],
        [0,0,1]
    ]
def rotation_matrix(t):
    return [
        [math.cos(t),-math.sin(t),0],
        [math.sin(t),math.cos(t),0],
        [0,0,1]
    ]

# from cat gee pee tee
def matrix_multiply(A, B):
    # Get the dimensions of the matrices
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    # Check if multiplication is possible
    if cols_A != rows_B:
        raise ValueError("Number of columns in A must match number of rows in B.")

    # Initialize the result matrix with zeros
    result = [[0] * cols_B for _ in range(rows_A)]

    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result

class SpinningGridAnimation(pixelstrip.Animation):
    """
    It draws a fish and moves it acros the screen alternating between 4 colors
    """
    #deines our different variables
    def __init__(self, framerate=60):
        pixelstrip.Animation.__init__(self)
        self.anchor_x=5
        self.anchor_y=5
        self.wait_time=1/framerate
        self.transform = [
            [1,0,0],
            [0,1,0],
            [0,0,1]
        ]
    def reset(self, strip):
        self.timeout = self.wait_time
        strip.clear()
        strip.show()
        # reset variables

    def draw(self, strip, delta_time):
        if self.is_timed_out():
            self.transform = matrix_multiply(self.transform,rotation_matrix(0.15))
            points=[]
            for y in range(-15,15):
                for x in range(-15,15):
                    pMat = [[x],[y],[1]]
                    pMat = matrix_multiply(self.transform,pMat)
                    px = int(pMat[0][0]*3)
                    py = int(pMat[1][0]*3)
                    if px<0 or px>=8 or py<0 or py>=32:
                        continue
                    points.append([px,py+8])
            strip.clear()
            for p in points:
                i=(p[0] if p[1]%2==0 else 7-p[0]) + 8*p[1]
                if i<0 or i>=8*32:
                    continue
                strip[i] = (20,0,25)
            strip.show()
            self.timeout = self.wait_time


if __name__ == "__main__":
    strip_gp15 = pixelstrip.PixelStrip(board.GP15, width=32, height=8, bpp=4, pixel_order=pixelstrip.GRB, options={pixelstrip.MATRIX_COLUMN_MAJOR, pixelstrip.MATRIX_ZIGZAG})
    strip_gp15.animation = SpinningGridAnimation()      
    while True:
        strip_gp15.draw()

