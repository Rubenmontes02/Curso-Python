import numpy as np

def saludar():
    print('hola, te saludo desde saludos.saludar()')

def prueba():
    print('Prueba de la nueva version')

def generarArray(numeros):
    return np.arange(numeros)

    
class Saludo:
    def __init__(self):
        print('Hola, te saludo desde Saludo__init__')



if __name__ == '__main__':
    print(generarArray(5))