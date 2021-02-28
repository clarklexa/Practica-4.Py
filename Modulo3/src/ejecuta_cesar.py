

# funcion propia
import cesar
from funciones_generales import validaciones as vali



# 4. Programa principal


k = vali.validar_ingreso_numero()

# solicitando cadena de texto
plaintext = input('Introduzca texto a cifrar: ')

# cifrando cadena de texto
ciphertext = cesar.cifrado_cesar(plaintext,k)
print("El texto cifrado es : {}".format(ciphertext))