import sqlite3

conexion = sqlite3.connect('ejemplo.db')

cursor = conexion.cursor()

# cursor.execute("CREATE TABLE usuarios (nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")

# cursor.execute("INSERT INTO usuarios VALUES ('Ruben', 20, 'ruben@ejemplo.com')")

# cursor.execute("SELECT * FROM usuarios")

# usuario = cursor.fetchone()

# print(usuario)


# usuarios = [
#    ('Mario', 51, 'mario@ejemplo.com'),
#    ('Pedro', 33, 'juan@ejemplo.com'),
#    ('Alberto', 27, 'alberto@ejemplo.com'),
#]
#cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)", usuarios)

cursor.execute("SELECT * FROM usuarios")

usuarios = cursor.fetchall()

for usuario in usuarios:
    print("Nombre: " + usuario[0] + "  Email: " + usuario[2])



conexion.commit()
conexion.close()