def get_list(fichero_palabras):
    fichero = open(fichero_palabras, mode="rt", encoding="utf-8")

    dic = {}
    lineas_fichero = f.readline()

    if lineas_fichero == "":
        raise ValueError("El fichero está vacío")
    else:
        contador_letras = 0
        while lineas_fichero != "" :
            palabras_linea = lineas_fichero.split(" ")
            for x in palabras_linea:
                if x.isalpha():
                    for i in x:
                        contador_letras = contador_letras + 1

                    lista_palabras = dic[contador_letras]

                    for j in lista_palabras:
                        if x != lista_palabras:
                            lista_palabras.append(x)

                            dic.update({contador_letras: lista_palabras})
                else:
                    raise ValueError("Se ha encontrado un elemento que no es una palabra, el fichero solo debe contener palabras.")
            
    return dic


def crear_lista_libros():

    
    
    lista_libros = []
    
    return lista_libros


def mas_antiguos(lista_libros):





lista_libros = crear_lista_libros()
mas_antiguos(lista_libros)


