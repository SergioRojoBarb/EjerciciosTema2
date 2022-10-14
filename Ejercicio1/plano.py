
from curses.ascii import isdigit


class Punto():

    coordenada_x_origen = 0
    coordenada_y_origen = 0

    num_a = int(input("Introduce la coordenada x de tu punto: "))
    coordenada_x = num_a
    while (num_a.isdigit()==False):
        print("Introduce sólo valores numéricos")
        num_a = int(input("Introduce la coordenada x de tu punto: "))
        coordenada_x = num_a
        break

    num_b = int(input("Introduce la coordenada y de tu punto: "))
    coordenada_y = num_b
    while (num_b.isdigit()==False):
        print("Introduce sólo valores numéricos")
        num_b = int(input("Introduce la coordenada x de tu punto: "))
        coordenada_y = num_b
        break


    def origen(self):
        if self.coordenada_x_origen and self.coordenada_y_origen:
            print("Tu punto está en el Origen 'O', punto(0,0)")
        else:
            return("Tu punto está en las coordenadas: ", "(",self.coordenada_x, self.coordenada_y,")")


    def coordenar_xy(self):

        num_a = int(input("Introduce la coordenada x de tu punto: "))
        coordenada_x = num_a
        print("Tu coordenada x es la", (coordenada_x)," )" )

        
        num_b = int(input("Introduce la coordenada y de tu punto: "))
        coordenada_y = num_b

        if self.coordenada_y >= 0 and self.coordenada_y <= 9:
            print("Tu coordenada y es la ( ,", coordenada_y, ")" )

        coordenadas_punto = (coordenada_x, coordenada_y)
        return("Tu punto es el ", coordenadas_punto)
    
'''
from Ejercicio1.introducir import numero

def coordenada(datoIntroducidox, datoIntroducidoy):
    coordenadas = print("Tu punto es el (", datoIntroducidox, ",", datoIntroducidoy, ")")
    return coordenadas
'''
        
