import string
import sys

def solicitar_introducir_cadena_X(invite):
    while True:
        print(invite, end=": ")
        datoIntroducidox = input()

        if len(datoIntroducidox) > 0:
            return datoIntroducidox

def solicitar_introducir_cadena_Y(invite):
    while True:
        print(invite, end=": ")
        datoIntroducidoy = input()

        if len(datoIntroducidoy) > 0:
            return datoIntroducidoy

'''
def solicitar_introducir_char(invite):
    while True:
        print(invite, end=": ")
        datoIntroducido = input()

        if len(datoIntroducido) == 0:
            print("Al menos debe indicar un carácter.", file=sys.stderr)
        elif len(datoIntroducido) > 1:
            print("Debe indicar un único carácter.", file=sys.stderr)
        else:
            return datoIntroducido

def solicitar_introducir_letra(invite):
    while True:
        datoIntroducido = solicitar_introducir_char

        if datoIntroducido in string.ascii_lowercase:
            return datoIntroducido
        elif datoIntroducido in string.ascii_uppercase:
            return datoIntroducido.lower()

def solicitar_introducir_palabra(invite):
    while True:
        '''



