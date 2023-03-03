import os
import helpers
import database as db

def iniciar():
    while True:
        helpers.limpiar_pantalla()

        print('====== Gestor de Clientes ======')
        print('1. Listar los clientes')
        print('2. Buscar cliente')
        print('3. Añadir un cliente')
        print('4. Modificar un cliente')
        print('5. Borrar un cliente')
        print('6. Salir del gestor\n')
        

        opcion = input('- ')
        helpers.limpiar_pantalla()

        if opcion == '1':
            print('Lista de clientes:\n')
            for cliente in db.Clientes.lista:
                print(cliente)

        if opcion == '2':
            print('Buscando cliente...\n')
            dni = helpers.leer_texto(9,9,'DNI: 8 numeros y una letra)').upper()
            cliente = db.Clientes.buscar(dni)
            print(cliente) if cliente else print('\nCliente no encontrado')

        if opcion == '3':
            print('Añadiendo cliente...\n')

            dni = None
            while True:
                dni = helpers.leer_texto(9,9,'DNI: 8 numeros y una letra)').upper()
                if helpers.dni_valido(dni, db.Clientes.lista):
                    break

            nombre = helpers.leer_texto(2,30,'Nombre: de 2 a 30 caracteres)').capitalize()
            apellido = helpers.leer_texto(2,30,'Apellido: de 2 a 30 caracteres)').capitalize()
            db.Clientes.crear(dni, nombre, apellido)
            print('\nCliente añadido')

        if opcion == '4':
            print('Modificando cliente...\n')
            dni = helpers.leer_texto(9,9,'DNI: 8 numeros y una letra)').upper()
            cliente = db.Clientes.buscar(dni)
            if cliente:
                nombre = helpers.leer_texto(2,30, f'Nombre: de 2 a 30 caracteres) [{cliente.nombre}]').capitalize()
                apellido = helpers.leer_texto(2,30, f'Apellido: de 2 a 30 caracteres) [{cliente.apellido}]').capitalize()
                db.Clientes.modificar(cliente.dni, nombre, apellido)
                print('\nCliente modificado')
            else:
                print('\nCliente no encontrado')


        if opcion == '5':
            print('Borrando cliente...\n')
            dni = helpers.leer_texto(9,9,'DNI: 8 numeros y una letra)').upper()
            print('\nCliente borrado') if db.Clientes.borrar(dni) else print('\nCliente no encontrado')

        if opcion == '6':
            print('Cerrando gestor...\n')
            break



        input('\n Presiona ENTER para continuar')

                   