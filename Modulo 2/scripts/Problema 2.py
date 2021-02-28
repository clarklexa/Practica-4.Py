import string

ALFABETO = string.ascii_lowercase

def validar_numero():
    try:
        k = int(input("\nDigite número para rotar: "))
        if k>=0:
            return k
        else:
            print("¡ERROR! {}. Digite números no negativos: ".format(1))
            return validar_numero()
    except:
        print("¡ERROR! {}. Digite bien el número: ".format(1))
        return validar_numero()

def cifrado_cesar(k):
    plaintext = input("\nDigite texto a cifrar: ")
    ciphertext = ''
    for l in plaintext:
        
        if l.lower() in ALFABETO:
            p = ALFABETO.find(l.lower())
            # algoritmo cesar
            c = (p + k) % 26
            
            if l.isupper():
                ciphertext += ciphertext.join(ALFABETO[c].upper())
            else:
                ciphertext += ciphertext.join(ALFABETO[c])
        else:
            ciphertext += ciphertext.join(l)
    return plaintext, ciphertext

k = validar_numero()
codigos = cifrado_cesar(k)
plaintext = codigos[0]
ciphertext = codigos[1]

print("\nPlaintext: {}".format(plaintext))
print("Ciphertext: {}".format(ciphertext))
print(0)