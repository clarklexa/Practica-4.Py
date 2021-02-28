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