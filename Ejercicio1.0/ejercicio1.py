
import math

class Punto:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        ch = "(" + str(self.x) + "," + str(self.y) + ")"
        return ch