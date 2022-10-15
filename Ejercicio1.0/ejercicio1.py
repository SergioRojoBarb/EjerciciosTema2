
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

    def v(self):
        Bx = int(input("Coordenadas de x: "))
        By = int(input("Coordenadas de y: "))
        vABx = Bx - self.x
        vABy = By- self.y
        vBAx = self.x - Bx
        vBAy = self.y - By

        print('El vector AB es: [', vABx,',',vABy,']')
        print('El vector AB es: [', vBAx,',',vBAy,']')

    def longitud(self):
        Bx = int(input("Coordenadas de x: "))
        By = int(input("Coordenadas de y: "))
        vx = Bx - self.x
        vy = By - self.y

        print('El vector AB es: [', vx,',',vy,']')

        longitud = math.sqrt(((vx*2) + (vy*2)))
        return longitud

class Rectangulo:

    def __init__(self, Ax, Ay, Bx, By):
        self.Ax = Ax
        self.Ay = Ay
        self.Bx = Bx
        self.By = By

    def base(self):
        return(abs(self.Bx - self.Ax))

    def altura(self):
        return(abs(self.By - self.Ay))

    def area(self):
        return self.base() * self.altura()

point = Punto(0,0)
print(point)
print(point.cuadrante())
print(point.v)
print(point.longitud)
r1 = Rectangulo(0,0,6,5)
print("La base es de ", r1.base())
print("La altura es de ", r1.altura())
print("El area es de ", r1.area())
