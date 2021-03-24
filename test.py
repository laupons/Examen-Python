import unittest
from examen import *

class Pruebas(unittest.TestCase):

    def test_mas_antiguos(self):
        lista = crear_lista_libros()

        lista_res = ["Años lluviosos", "La vide de Pepa", "Kira y el misterio del dragón"]

        self.assertEqual(mas_antiguos(lista), lista_res)

    def test_mas_antiguos_anyo_incorrecto(self):
        lista = crear_lista_libros()

        libro6 = Libro("Kayla", "Kira y el misterio del dragón", 1898)

        lista.append(libro6)

        self.assertRaisesRegexp(ValueError, "El año del libro no puede ser anterior a 1900", mas_antiguos, lista)

     def test_mas_antiguos_anyo_incorrecto_2(self):
        lista = crear_lista_libros()

        libro6 = Libro("Kayla", "Kira y el misterio del dragón", 2058)

        lista.append(libro6)

        self.assertRaisesRegexp(ValueError, "El año del libro no puede ser posterior a 2021", mas_antiguos, lista)




class Suite(unittest.TestSuite):

    def __init__(self):
        super(Suite, self).__init__()
        self.addTest(Pruebas('test_mas_antiguos'))
        self.addTest(Pruebas('test_mas_antiguos_anyo_incorrecto'))
        self.addTest(Pruebas('test_mas_antiguos_anyo_incorrecto_2'))



if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    my_suite = Suite()
    runner.run(my_suite)
