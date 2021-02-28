def promedio_total(promedio):
    suma = 0
    for i in range(len(promedio)):
        suma += promedio[i]
    promedio_final = suma/len(promedio)
    return promedio_final