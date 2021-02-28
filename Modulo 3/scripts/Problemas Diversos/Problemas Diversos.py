#PROBLEMA 1
from Modulo_Problema1 import modulo_1


n = modulo_1.cantidad_alumnos()

lista_alumnos = modulo_1.listar_alumnos(n)

print("\n***LISTADO***")
for i in lista_alumnos:
    print("Nombre:",i["nombre"])
    print("Nota 1:",i["nota1"])
    print("Nota 2:",i["nota2"])
    print("Nota 3:",i["nota3"])



#PROBLEMA 2
from Modulo_Problema2 import modulo_2

promedio = modulo_2.promedios(lista_alumnos)
cantidades = modulo_2.aprobado_desaprobado(promedio)
aprobados = cantidades[0]
desaprobados = cantidades[1]

print("Aprobados {}".format(aprobados))
print("Desaprobados {}".format(desaprobados))



#PROBLEMA 3
from Modulo_Problema3 import modulo_3


promedio_final = modulo_3.promedio_total(promedio)

print("El promedio final del curso es {}".format(promedio_final))


#PROBLEMA 4

from Modulo_Problema4 import modulo_4


indice_mayor = modulo_4.promedio_alto(promedio)
indice_menor = modulo_4.promedio_bajo(promedio)

print("El alumno {} tuvo el promedio más alto con {}".format(lista_alumnos[indice_mayor]["nombre"],promedio[indice_mayor]))
print("El alumno {} tuvo el promedio más bajo con {}".format(lista_alumnos[indice_menor]["nombre"],promedio[indice_menor]))


#PROBLEMA 5

from Modulo_Problema5 import modulo_5

nombre = input("Digite nombre completo o parcial del alumno a buscar: ")

indices = modulo_5.buscar_alumno(nombre, lista_alumnos)

if type(indices) is list:
    print("\n**Alumnos Encontrados**")
    for i in range(len(indices)):
        print("Nombre: {}".format(lista_alumnos[indices[i]]["nombre"]))
        print("Nota 1: {}".format(lista_alumnos[indices[i]]["nota1"]))
        print("Nota 2: {}".format(lista_alumnos[indices[i]]["nota2"]))
        print("Nota 3: {}".format(lista_alumnos[indices[i]]["nota3"]))
        print("Promedio: {}".format(promedio[indices[i]]))
        print("\n")
else:
    print(indices)