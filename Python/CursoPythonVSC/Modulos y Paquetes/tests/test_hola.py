import unittest
from mensajes.hola.saludos import generarArray

class PruebasHola(unittest.TestCase()):
    def test_generarArray(self):
        np.testing.assert_array_equal(
            np.array([0,1,2,3,4,5]),
            generarArray(6))



from mensajes.hola.saludos import *
from mensajes.adios.despedidas import *

saludar()

Saludo()

despedir()

Despedir()

