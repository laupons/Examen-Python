def get_list(fichero_palabras):
    fichero = open(fichero_palabras, mode="rt", encoding="utf-8")

    dic = {}
    lineas_fichero = f.readline()
    
    contador_letras = 0

    while lineas_fichero != "" :
        palabras_linea = lineas_fichero.split()
        for x in palabras_linea:
            for i in x:
                contador_letras = contador_letras + 1
                


def mas_antiguos():

