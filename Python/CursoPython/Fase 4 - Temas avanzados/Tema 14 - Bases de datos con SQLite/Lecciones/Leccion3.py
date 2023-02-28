import sqlite3

conexion = sqlite3.connect('usuarios_autoincremental.db')
cursor = conexion.cursor()

cursor.execute("DELETE FROM usuarios_autoincremental")

usuarios = cursor.fetchall()
for usuario in usuarios:
    print(usuario)

conexion.commit()
conexion.close()