'''
import sys

MIN = 0
MAX = 1000

def solicitar_introducir_numero_X(invite):
    while True:
        print(invite, end=": ")
        datoIntroducidox = input()

        try:
            datoIntroducidox = int(datoIntroducidox)

        except:
            print("Solo estan autorizados los caracteres [0-1000].", file=sys.stderr)

        else:
            return datoIntroducidox

def solicitar_introducir_numero_Y(invite):
    while True:
        print(invite, end=": ")
        datoIntroducidoy = input()

        try:
            datoIntroducidoy = int(datoIntroducidoy)

        except:
            print("Solo estan autorizados los caracteres [0-9].", file=sys.stderr)

        else:
            return datoIntroducidoy

'''
'''
def solicitar_introducir_numero_extremo(invite, minimum=MIN, maximum=MAX):
    invite="{} entre {} y {} incluídos".format(invite, minimum, maximum)
    while True:
        datoIntroducido = solicitar_introducir_numero(invite)
        if minimum <= datoIntroducido <= maximum:
            return datoIntroducido
            '''