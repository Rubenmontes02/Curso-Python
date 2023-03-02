from tkinter import *
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


root = Tk()

root.title('Primer App')

imagen = PhotoImage(file=resource_path("res/relax.png"))

Label(image=imagen).pack()

root.mainloop()


#  COMANDO PARA CREAR APP
#  pipenv run pyinstaller programa.py --windowed --onefile --clean --add-data res;res --ico res/gato.ico