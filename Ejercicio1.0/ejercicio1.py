
import math

class Punto:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        ch = "(" + str(self.x) + "," + str(self.y) + ")"
        return ch

    def cuadrante(self):
        
        cuadrante = None

        if self.x > 0 and self.y > 0:
            cuadrante = "1er cuadrante"

        elif self.x > 0 and self.y < 0:
            cuadrante = "4º cuadrante"

        elif self.x < 0 and self.y > 0:
            cuadrante = "2º cuadrante"

        elif self.x < 0 and self.y < 0:
            cuadrante = "3er cuadrante"

        elif self.x == 0 and self.y != 0:
            cuadrante = "En el eje de ordenadas"

        elif self.x != 0 and self.y == 0:
            cuadrante = "En el eje de abcisas"

        elif self.x == 0 and self.y == 0:
            cuadrante = "En el origen"
        
        return cuadrante
        
        






