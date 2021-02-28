#PROBLEMA 1
def ingresar_nota():

    try:
        nota = float(input("Introduce la nota(0 - 10): "))
        
        if nota >=0 and nota <= 10:
            return nota  # Importante romper la iteración si todo ha salido bien
        else:
            print('nota fuera del rango')
            return ingresar_nota()
    except:
        print("Ha ocurrido un error, introduce bien la nota")
        return ingresar_nota()



def listar_alumnos(cantidad_alumnos):
    lista_alumnos = []
    for i in range(cantidad_alumnos):
        alumno = {}
        # Ingreso de nombre de alumno
        alumno['nombre'] = input('Ingrese el nombre del alumno {}: '.format(i+1))
    
        # ingreso de notas
        alumno['nota1'] = ingresar_nota()
        alumno['nota2'] = ingresar_nota()
        alumno['nota3'] = ingresar_nota()
    
        # agregando alumno a lista alumnos
        lista_alumnos.append(alumno)
    
    return lista_alumnos


def cantidad_alumnos():
    try:
        n = int(input('Cantidad de alumnos a ingresar: '))
        if n>0:
            return n
        else:
            print("Debe digitar canttidades positivas")
            return cantidad_alumnos()
    except:
        print("¡ERROR! Digite un número válido")
        return cantidad_alumnos()

n = cantidad_alumnos()

lista_alumnos = listar_alumnos(n)

print("\n***LISTADO***")
for i in lista_alumnos:
    print("Nombre:",i["nombre"])
    print("Nota 1:",i["nota1"])
    print("Nota 2:",i["nota2"])
    print("Nota 3:",i["nota3"])



#PROBLEMA 2
def promedios(lista_alumnos):
    promedio = []
    for i in range(len(lista_alumnos)):
        valor = (lista_alumnos[i]["nota1"]+lista_alumnos[i]["nota2"]+lista_alumnos[i]["nota3"])/3
        promedio.append(valor)
    return promedio

def aprobado_desaprobado(promedio):
    a = 0
    d = 0
    for i in range(len(promedio)):
        if promedio[i]>=4:
            a+=1
        else:
            d +=1
    return a,d

promedio = promedios(lista_alumnos)
cantidades = aprobado_desaprobado(promedio)
aprobados = cantidades[0]
desaprobados = cantidades[1]

print("Aprobados {}".format(aprobados))
print("Desaprobados {}".format(desaprobados))



#PROBLEMA 3
def promedio_total(promedio):
    suma = 0
    for i in range(len(promedio)):
        suma += promedio[i]
    promedio_final = suma/len(promedio)
    return promedio_final

promedio_final = promedio_total(promedio)

print("El promedio final del curso es {}".format(promedio_final))


#PROBLEMA 4
def promedio_alto(promedio):
    may = max(promedio)
    indice = promedio.index(may)
    return indice


def promedio_bajo(promedio):
    men = min(promedio)
    indice = promedio.index(men)
    return indice


indice_mayor = promedio_alto(promedio)
indice_menor = promedio_bajo(promedio)

print("El alumno {} tuvo el promedio más alto con {}".format(lista_alumnos[indice_mayor]["nombre"],promedio[indice_mayor]))
print("El alumno {} tuvo el promedio más bajo con {}".format(lista_alumnos[indice_menor]["nombre"],promedio[indice_menor]))


#PROBLEMA 5

def buscar_alumno(nombre,lista_alumnos):
    indices_buscados = []
    for i in range(len(lista_alumnos)):
        count = 0
        for t in range(len(nombre)):
            if nombre[t].lower() == lista_alumnos[i]["nombre"][t].lower():
                count += 1
            
        if count == len(nombre):
                indices_buscados.append(i)
    
    if len(indices_buscados)>0:
        return indices_buscados
    else:
        return "\n**NO SE ENCONTRARON ALUMNOS**"

nombre = input("Digite nombre completo o parcial del alumno a buscar: ")

indices = buscar_alumno(nombre, lista_alumnos)

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