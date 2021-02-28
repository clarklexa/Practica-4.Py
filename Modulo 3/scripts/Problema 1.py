import string

numeros = string.digits



def caracteres_validos():
    count = 0
    numero_tarjeta = input("Digite tarjeta (máximo 16 dígitos): ")
    for i in range(len(numero_tarjeta)):
        if numero_tarjeta[i] in numeros:
            count += 1
    if count == len(numero_tarjeta):
        return numero_tarjeta
    else:
        print("Digitos incorrectos\n")
        return caracteres_validos()
    

def luhn(ccn):
    c = [int(x) for x in ccn[::-2]]
    u2 = [(2*int(y))//10+(2*int(y))%10 for y in ccn[-2::-2]]
    return sum(c+u2)%10 == 0


def tipo_tarjeta(ccn,bol):
    if bol:
        if ccn[0] == '3':
            if ccn[1]== '7':
                return "AMEX"
            elif ccn[1]=='0':
                return "DINNERS CLUB"
            elif ccn[0] == '5':
                return "JCB"

        elif ccn[0] == '6':
            return "DISCOVER"

        elif ccn[0] == '2' or ccn[0] == '5':
            return "MASTERCARD"
        
        elif ccn[0] == '4':
            return "VISA"
            
    else:
        return "INVALID"


cuenta_tarjeta = caracteres_validos()
bol = luhn(cuenta_tarjeta)
tipo = tipo_tarjeta(cuenta_tarjeta , bol)

print("Su tarjeta es "+tipo)