from tkinter import *

def sumar():
    resultado.set(float(n1.get()) + float(n2.get()))
    borrar()

def restar():
    resultado.set(float(n1.get()) - float(n2.get()))
    borrar()


def multiplicar():
    resultado.set(float(n1.get()) * float(n2.get()))
    borrar()


def dividir():
    resultado.set(float(n1.get()) / float(n2.get()))
    borrar()


def borrar():
    n1.set("")
    n2.set("")


root = Tk()
root.title("Sumar")
root.config(padx=5, pady=5)


n1 = StringVar()
n2 = StringVar()
resultado = StringVar()

Label(root, text="Numero 1: ").pack()
Entry(root, justify="center", textvariable=n1).pack()          # Primer Numero

Label(root, text="Numero 2: ").pack()
Entry(root, justify="center", textvariable=n2).pack()          # Segundo Numero

Label(root, text="Resultado: ").pack()
Entry(root, justify="center", textvariable=resultado, state=DISABLED).pack()   # Resultado

Button(root, text="Sumar", command=sumar).pack()
Button(root, text="Restar", command=restar).pack()
Button(root, text="Multiplicar", command=multiplicar).pack()
Button(root, text="Dividir", command=dividir).pack()



root.mainloop()