from tkinter import *

root = Tk()
root.title("Label")

# Variables dinamicas


texto = StringVar()
texto.set("Un nuevo texto")

Label(root, text= "Una Etiqueta").pack(anchor ="nw")
label = Label(root, text= "Otra Etiqueta")
label.pack(anchor="center")
Label(root, text= "Otra Etiqueta Mas").pack(anchor ="se")

label.config(bg="lightgreen", fg="blue", font=("Verdana", 18))
label.config(textvariable = texto)



imagen = PhotoImage(file = "imagen.gif")
Label(root, image = imagen, bd=0).pack(side = "left")





root.mainloop()