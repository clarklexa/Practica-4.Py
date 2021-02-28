import string            
import random


abecedario = string.ascii_lowercase
clave = ""
ciphertext = ""
plaintext = ""


def generar_clave():
    clave_generada = ""
    clave = []
    while True:
        aleatorio = random.randint(0,25)
        clave += list(abecedario[aleatorio])
        clave = list(set(clave))
        if len(clave) == 26:
            for i in range(26):
                clave_generada += clave[i]
            
            break
    
    return clave_generada


def descifrar_palabra(clave):
    if len(clave) > 0:
        ciphertext = ""
        plaintext = input("Digite texto a descifrar: ")
        for palabra in plaintext:
            if palabra.lower() in abecedario:
                index = abecedario.index(palabra.lower())
                if palabra.islower():
                    ciphertext += clave[index]
                else:
                    ciphertext += clave[index].upper()
            else:
                ciphertext += palabra
        return plaintext , ciphertext
    else:
        return 1

while True:
    print("\n***MENU DEL CIFRADO***")
    print("1.- Generar clave de 26 caracteres")
    print("2.- Generar Cifrado")
    print("3.- Mostrar")
    print("4.- Salir")
    opcion = input("Opción: ")

    if opcion == '1':
        clave = generar_clave()
        print("***CLAVE GENERADA*** \n{}".format(0))
    elif opcion == '2':
        codigos = descifrar_palabra(clave)
        if codigos != 1:
            plaintext = codigos[0]
            ciphertext = codigos[1]
            print("\n***TEXTO CIFRADO***")
        else:
            print(codigos)

    elif opcion == '3':
        if plaintext != "" and ciphertext != "": 
            print("\nClave: {}".format(clave))
            print("\nPlaintext: {}".format(plaintext))
            print("\nCiphertext: {}".format(ciphertext))
            print("\n",0)
        else:
            print(1)

    elif opcion == '4':
        print("\n¡HASTA LUEGO!")
        break
    else:
        print("\nDIGITE OPCION VALIDA")