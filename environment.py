import numpy as np

class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = np.zeros((height,width),dtype=np.int8)

    def get_square(self, x, y):
        return self.grid[y, x]  # y first, then x

    def colorSquare(self, color, x, y):
        self.grid[y, x] = color  # y first, then x