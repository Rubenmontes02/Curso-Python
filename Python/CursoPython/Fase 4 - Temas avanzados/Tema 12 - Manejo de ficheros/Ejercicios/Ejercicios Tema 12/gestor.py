from io import open
import pickle

class Personaje:
    def __init_(self, nombre, vida, ataque, defensa, alcance):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance

    def __str__(self):
        return '{} -> Vida: {}, Ataque: {}, Defensa: {}, Alcance: {}'.format(self.nombre, self.vida, self.ataque, self.defensa, self.alcance)


class Gestor:
    
    personajes = []

    # Constructor de clase
    def __init__(self, personajes=[]):
        self.cargar()
            
    def agregar(self,p):

        for pTemp in self.personajes:
            if pTemp.nombre == p.nombre:
                return
      
        self.personajes.append(p)
        self.guardar()
        

    def borrar(self,nombre):

        for pTemp in self.personajes:
            if pTemp.nombre == p.nombre:                        
                self.personajes.remove(pTemp)
                self.guardar()
                print('\nPersonaje {} borrado'.format(nombre))
                return


    def mostrar(self):
        if len(self.personajes) == 0:
            print('El gestor está vacio')
            return
        else:
            for p in self.personajes:
                print(p)


     
    def cargar(self):        
        fichero = open('Personajes.pckl', 'ab+')
        fichero.seek(0)
        try:
            self.personajes = pickle.load(fichero)
        except:
            #print('El fichero está vacio')
            pass
        finally:
            fichero.close()
            del(fichero)  # Solo eliminamos el fichero cuando estemos trabajando en jupyter
            print('Se han cargado {} persoanjes'.format(len(self.personajes)))
            
    def guardar(self):
        fichero = open('Gestor.pckl', 'wb')
        pickle.dump(self.personajes, fichero)
        fichero.close()
        del(fichero)
            

G = Gestor()
G.mostrar()

G.agregar(Personaje("Guerrero", 2, 4, 2, 4))
G.agregar(Personaje("Arquero", 2, 4, 1, 8))


G.mostrar()
