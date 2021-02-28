# 1.importacion de librerias
import string




ALFAFETO = string.ascii_lowercase

# 3. declacion de funciones
def cifrado_cesar(plaintext,k):
    """
    Funcion que permite realizar el cifrado cesar de cierta cadena de carácteres.

    Parameters
    ----------
    plaintext : str
    k : int

    Returns
    -------
    ciphertext : str
        Texto según cifrado cesar

    """

    ciphertext = ''
    for l in plaintext:
    
        if l.lower() in ALFAFETO:
            p = ALFAFETO.find(l.lower())
            # algoritmo cesar
            c = (p + k) % 26

            if l.isupper():
                ciphertext += ciphertext.join(ALFAFETO[c].upper())
            else:
                ciphertext += ciphertext.join(ALFAFETO[c])
        else:
            ciphertext += ciphertext.join(l)

    return ciphertext

# 4. Programa principal
