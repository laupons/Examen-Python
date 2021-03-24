import unittest
from examen import *

class Pruebas(unittest.TestCase):

    def test_mas_antiguos(self):
        lista = crear_lista_libros()

        lista_res = ["Años lluviosos", "La vide de Pepa", "Kira y el misterio del dragón"]

        self.assertEqual(mas_antiguos, lista_res)

    def test_mas_antiguos_anyo_incorrecto(self):
        lista = crear_lista_libros()

        libro6 = Libro("Kayla", "Kira y el misterio del dragón", 1898)

        lista_libros.append(libro6)
        

        self.assertRaisesRegexp(ValueError, "El valor del primer caracter en el numero de vuelo tiene que ser una letra.", __init__, "2A117", Aircraft("G-EUAH", "Airbus A319", 22, 6)




class Suite(unittest.TestSuite):

    def __init__(self):
        super(Suite, self).__init__()
        self.addTest(Pruebas('test_mas_antiguos'))

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    my_suite = Suite()
    runner.run(my_suite)
