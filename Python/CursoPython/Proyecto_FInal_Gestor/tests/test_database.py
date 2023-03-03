import helpers
import csv
import copy
import config
import unittest
import database as db

class TestDatabase(unittest.TestCase):

    def setUp(self):
        db.Clientes.lista = [
            db.Cliente('11111111A', 'Ruben', 'Montes'),
            db.Cliente('22222222B', 'Juan', 'Romero'),
            db.Cliente('12222222A', 'Pedro', 'Perez'),
        ]


    def test_buscar_clientes(self):
        clientes_existentes = db.Clientes.buscar('11111111A')
        clientes_inexistentes = db.Clientes.buscar('30000000A')
        self.assertIsNotNone(clientes_existentes)
        self.assertIsNone(clientes_inexistentes)


    def test_crear_cliente(self):

        nuevo_cliente = db.Clientes.crear('33000000A', 'Fernando', 'Alonso')
        self.assertEqual(len(db.Clientes.lista), 4)
        self.assertEqual(nuevo_cliente.dni, '33000000A')
        self.assertEqual(nuevo_cliente.nombre, 'Fernando')
        self.assertEqual(nuevo_cliente.apellido, 'Alonso')


    def test_modificar_cliente(self):
        cliente_a_modificar = copy.copy(db.Clientes.buscar('12222222A'))
        cliente_modificado = db.Clientes.modificar('12222222A', 'Alberto', 'Garcia')
        self.assertEqual(cliente_a_modificar.nombre, 'Pedro')
        self.assertEqual(cliente_modificado.nombre, 'Alberto')

    def test_borrar_cliente(self):
        cliente_borrado = db.Clientes.borrar('12222222A')
        cliente_buscado = db.Clientes.buscar('12222222A')
        self.assertEqual(cliente_borrado.dni, '12222222A')
        self.assertIsNone(cliente_buscado)


    def test_dni_valido(self):
        self.assertTrue(helpers.dni_valido('00000000Q', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('3123123', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('UYTGHFRT2', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('11111111A', db.Clientes.lista))

        
    def test_escritura_csv(self):
        db.Clientes.borrar('11111111A')
        db.Clientes.borrar('12222222A')
        db.Clientes.modificar('22222222B', 'Roberto', 'Montero')

        dni, nombre, apellido = None, None, None
        with open(config.DATABASE_PATH, newline='\n') as fichero:
            reader = csv.reader(fichero, delimiter=';')
            dni, nombre, apellido = next(reader)

        self.assertEqual(dni, '22222222B')
        self.assertEqual(nombre, 'Roberto')
        self.assertEqual(apellido, 'Montero')

