import menu
import sys
import interfaz

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "-t":
        menu.iniciar()
    else:
        app = interfaz.MainWindow()
        app.mainloop()
