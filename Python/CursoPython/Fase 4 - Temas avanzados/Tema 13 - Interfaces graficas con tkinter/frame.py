from tkinter import *

# Configuracion de la raiz
root = Tk()
root.title('Hola Mundo')
root.iconbitmap('hola.ico')
root.resizable(True, True)

frame = Frame(root)
frame.pack(fill="both", expand=1) # side="bottom", anchor="w"  (Para anclar el frame a un lugar especifico)

frame.config(width=480, height=320)
frame.config(cursor="pirate")
frame.config(bg="lightblue")
frame.config(bd=25)
frame.config(relief="sunken")



root.config(cursor="arrow")
root.config(bg="aqua")
root.config(bd=15)
root.config(relief="ridge")




# Finalmente ejecutamos el bucle de la raiz
root.mainloop()