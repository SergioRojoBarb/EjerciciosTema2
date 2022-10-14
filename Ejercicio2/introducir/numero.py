import sys

MIN = 0
MAX = 9

def solicitar_introducir_numero(invite):
    while True:
        print(invite, end=": ")
        datoIntroducido = input()

        try:
            datoIntroducido = int(datoIntroducido)

        except:
            print("Solo estan autorizados los caracteres [0-9].", file=sys.stderr)

        else:
            return datoIntroducido



def solicitar_introducir_numero_extremo(invite, minimum=MIN, maximum=MAX):
    invite="{} entre {} y {} incluídos".format(invite, minimum, maximum)
    while True:
        datoIntroducido = solicitar_introducir_numero(invite)
        if minimum <= datoIntroducido <= maximum:
            return datoIntroducido
