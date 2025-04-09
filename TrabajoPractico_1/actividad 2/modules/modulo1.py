
class Nodo:
    def __init__(self, datoInicial):
        self.dato = datoInicial
        self.siguiente = None
    
    def obtenerDato(self):
        return self.dato
    
    def obtenerSiguiente(self):
        return self.siguiente
    
    def asignarDato(self,nuevoDato):
        self.dato = nuevoDato

    def asignarSiguiente(self, nuevodatoSig):
        self.siguiente = nuevodatoSig


class ListaNoOrdenada:
    def __init__(self):
        self.cabeza = None

    def estaVacia(self):
        return self.cabeza == None




def esta_vacia():
    pass

def __len__():
    pass

def agregar_al_inicio(item):
    pass

def agregar_al_final(item):
    pass

def insertar(item, posicion):
    pass

def extraer(posicion):
    pass

def copiar():
    pass

def invertir():
    pass

def concatenar(lista):
    pass

def __add__(lista):
    pass
