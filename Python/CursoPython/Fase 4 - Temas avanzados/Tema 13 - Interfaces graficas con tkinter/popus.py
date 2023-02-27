from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog


root = Tk()

def test():
#    MessageBox.showinfo("Infromación", "Informacion sobre la ventana")

#    MessageBox.showwarning("Alerta", "Solo para Administradores")

#    MessageBox.showerror("Error!", "Ha ocurrido un error inesperado")

#    resultado = MessageBox.askquestion("Salir", "¿Estas seguro que quieres salir sin guardar?")
#    if resultado == "yes":
#        root.quit()

#    resultado = MessageBox.askokcancel("Sobreescribir", "¿Sobreescribir fichero?")
#    if resultado == True:
#        root.quit()

#    resultado = MessageBox.askyesno()("Salir", "¿Estas seguro que quieres salir sin guardar?")
#    if resultado == True:
#        root.quit()

#    resultado = MessageBox.askretrycancel("Reintentar", "No se puede conectar")
#    if resultado == True:
#        root.quit()

#    color = ColorChooser.askcolor(title= "Elije un color")
#    print(color)

#    ruta = FileDialog.askopenfile(title= "Abrir un fichero", initialdir= "C:",
#    filetypes= (("Fichero de texto", "*.txt"),
#    ("Fichero de texto avanzado", "*.txt2"),
#    ("Todos los ficheros posibles", "*.*")))
#    print(ruta)

    fichero = FileDialog.asksaveasfile(title= "Guardar fichero", mode= "w", defaultextension= "*.txt")   # Equivale a open('ruta', 'w')
    print(fichero)



Button(root, text="Click", command=test).pack()




root.mainloop()