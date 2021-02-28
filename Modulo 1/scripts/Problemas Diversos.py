# PROBLEMA 1
ahorro = float(input("Digite depósito: "))
primero = round(ahorro + ahorro*0.04,2)
segundo = round(primero + primero*0.04,2)
tercero = round(segundo + segundo*0.04,2)

print("Ahorro del primer año",primero)
print("Ahorro del segundo año",segundo)
print("Ahorro del tercer año",tercero)

#PROBLEMA 2
print("Encuentre las soluciones de la siguiente ecuación cuadrática: ax^2 + bx + c = 0")
a = float(input("Digite primer coeficiente: "))
b = float(input("Digite segundo coeficiente: "))
c = float(input("Digite tercer coeficiente: "))

if a!=0:
    discriminante = b**(2)-4*a*c
    if discriminante>0:
        print("Tiene soluciones diferentes")
        x1 = (-b+discriminante**(1/2))/(2*a)
        x2 = (-b-discriminante**(1/2))/(2*a)
        print("Las soluciones son {} y {}".format(x1,x2))
    elif discriminante == 0:
        x = -b/(2*a)
        print("La solución única es {}".format(x))
    else:
        print("La ecuación no tiene solución real")
else:
    print("La ecuación no es cuadrática")