import sqlite3

conexion = sqlite3.connect("usuarios_autoincremental.db")
cursor = conexion.cursor()


#cursor.execute("CREATE TABLE usuarios(dni VARCHAR(9) PRIMARY KEY, nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")

#usuarios = [
#    ('11111111A', 'Ruben', 20, 'ruben@ejemplo.com'),
#    ('22222222B', 'Mario', 51, 'mario@ejemplo.com'),
#    ('33333333C', 'Pedro', 33, 'juan@ejemplo.com'),
#    ('44444444D', 'Alberto', 27, 'alberto@ejemplo.com'),
#]

#cursor.executemany("INSERT INTO usuarios VALUES (?,?,?,?)", usuarios)

#cursor.execute("INSERT INTO usuarios VALUES ('55555555F', 'Alberto', 27, 'alberto@ejemplo.com')")

#cursor.execute("""
#    CREATE TABLE productos(
#        id INTEGER PRIMARY KEY AUTOINCREMENT, 
#        nombre VARCHAR(100) NOT NULL, 
#        marca VARCHAR (50) NOT NULL, 
#        precio FLOAT NOT NULL
#    )""")

#productos = [
#    ('Teclado', 'Logitech', 32.99),
#    ('Raton', 'Corsair', 48.45)
#]

#cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)

#cursor.execute("SELECT * FROM productos")

#productos = cursor.fetchall()
#for producto in productos:
#    print(producto)


#cursor.execute("""
#    CREATE TABLE usuarios_autoincremental(
#        id INTEGER PRIMARY KEY AUTOINCREMENT, 
#        dni VARCHAR(9) UNIQUE NOT NULL, 
#        nombre VARCHAR(100) NOT NULL, 
#        edad INTEGER NOT NULL, 
#        email VARCHAR(100) NOT NULL
#    )
#""")

#usuarios = [
#    ('11111111A', 'Ruben', 20, 'ruben@ejemplo.com'),
#    ('22222222B', 'Mario', 51, 'mario@ejemplo.com'),
#    ('33333333C', 'Pedro', 33, 'juan@ejemplo.com'),
#    ('44444444D', 'Alberto', 27, 'alberto@ejemplo.com'),
#]

#cursor.executemany("INSERT INTO usuarios_autoincremental VALUES (null, ?,?,?,?)", usuarios)

cursor.execute("INSERT INTO usuarios_autoincremental VALUES (null, '11111111B', 'Marta', 42, 'marta@ejemplo.com')")

conexion.commit()
conexion.close()