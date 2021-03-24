from libro import *
from autor import *

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

    libro1 = Libro("Maria", "Años lluviosos", 1986)
    libro2 = Libro("Julia", "Corte de tinieblas", 2016)
    libro3 = Libro("Mike", "El señor de las moscas", 2018)
    libro4 = Libro("Juan", "La vide de Pepa", 2005)
    libro5 = Libro("Kayla", "Kira y el misterio del dragón", 1998)

    lista_libros = []

    lista_libros.append(libro1)
    lista_libros.append(libro2)
    lista_libros.append(libro3)
    lista_libros.append(libro4)
    lista_libros.append(libro5)

    
    return lista_libros


def mas_antiguos(lista_libros, anyo):
    lista_titulos = []
    for x in lista_libros:
        anyo_libro = x.get_anyo()
        if anyo_libro < 1900:
            raise ValueError("El año del libro no puede ser anterior a 1900")
        elif anyo_libro > 2021:
            raise ValueError("El año del libro no puede ser posterior a 2021")
        else:
            if anyo_libro <= anyo:
                titulo_libro = x.get_titulo()
                lista_titulos.append(lista_titulos)
    return lista_titulos


get_list("palabras.txt")
lista_libros = crear_lista_libros()
mas_antiguos(lista_libros, 2005)


