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