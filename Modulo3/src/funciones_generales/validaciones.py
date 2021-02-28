


def validar_ingreso_numero(n='a'):
    while True:
        try:
            n = int(input("Introduce un número: "))
            return n
        except:
            print("Ha ocurrido un error, introduce bien el número")



#print(validar_ingreso_numero())
