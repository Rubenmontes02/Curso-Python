from tkinter import *
from tkinter import filedialog as FiledDialog
from io import open

# La utiliazremos para almacenar la ruta de un fichero
ruta = ""  


def nuevo():
    global ruta
    mensaje.set("Nuevo fichero")
    ruta = ""
    texto.delete(1.0, END)
    root.title("Mi Editor")

def abrir():
    global ruta
    mensaje.set("Abrir fichero")
    ruta = FiledDialog.askopenfilename(
        initialdir='.', 
        filetype=(("Ficheros de texto", "*.txt"),),
        title= "Abrir un fichero de texto")

    if ruta != "":
        fichero = open(ruta, "r")
        contenido = fichero.read()
        texto.delete(1.0, END)
        texto.insert("insert",contenido)
        fichero.close()
        root.title(ruta + " -Mi Editor- ")


def guardar():
    mensaje.set("Guardar fichero")
    if ruta != "":
        contenido = texto.get(1.0, 'end-1c')  # 'end-1c' significa que se elimine hasta el ultimo caracter menos el ultimo
        fichero = open(ruta, "w+")
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")

    else:
        guardarComo()


def guardarComo():
    global ruta
    mensaje.set("Guardar como")
    fichero = FiledDialog.asksaveasfile(title="Guardar como", mode="w", defaultextension=".txt")
    if fichero!= None:
        ruta = fichero.name
        contenido = texto.get(1.0, 'end-1c')  # 'end-1c' significa que se elimine hasta el ultimo caracter menos el ultimo
        fichero = open(ruta, "w+")
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")
    else:
        mensaje.set("Guardado cancelado")
        ruta = ""

root = Tk()
root.title("Mi Editor")


# Menú superior

menuBar = Menu(root)
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="Nuevo", command=nuevo)


fileMenu.add_command(label="Abrir", command=abrir)


fileMenu.add_command(label="Guardar", command=guardar)


fileMenu.add_command(label="Guardar como", command=guardarComo)


fileMenu.add_separator()
fileMenu.add_command(label="Salir", command=root.quit)
menuBar.add_cascade(menu=fileMenu, label="Archivo")


# Caja de texto central
texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6, pady=4, font=("Consolas", 12))

# Monitor inferior
mensaje = StringVar()
mensaje.set("Bienvenido a tu editor")
monitor = Label(root, textvar=mensaje, justify="left")
monitor.pack(side="left")



root.config(menu=menuBar)

root.mainloop()