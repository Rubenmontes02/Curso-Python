from setuptools import setup

setup(
    name='Mensajes',
    version='2.0',
    description='Un paquete para saludar y despedir',
    author='Ruben Montes Gonzalez',
    author_email='hola@.ruben.com',
    url='hola.com',
    packages=['mensajes','mensajes.hola','mensajes.adios'],
    scripts=['test.py'],

)

