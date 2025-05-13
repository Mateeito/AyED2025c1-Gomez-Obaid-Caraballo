

class NodoAVL:
    def __init__(self, fecha, temperatura): #Al momento de crear un Nodo le tenemos que pasar al constructor tanto la fecha en la que se ingresa el dato, como la temperatura de ese dia
        self.fecha = fecha                  #Esto lo hacemos con datetime
        self.temperatura = temperatura      #Es un flotante
        self.altura = 1                     #Esta altura lo que hace es decirnos la cantidad de "pisos" o "niveles" que hay desde este nodo hasta el nivel mas profundo del arbol avl. por ejemplo, si el nodo no tiene hijos: altura = 1, si el nodo tiene un hijo altura = 1 + altura del hijo, si tiene 2 hijos seria altura = 1 + altura del hijo izquierdo + altura del hijo derecho (donde, la altura de cada hijo, depende a su vez de la cantidad de hijos que estos tengan, ya que con ellos se repite el mismo proceso)  
        self.derecha = None                 #Rama derecha del arbol, apunta a fechas anteriores a la de este nodo, arranca siendo None
        self.izquierda = None               #Rama derecha del arbol, apunta a fechas posteriores a la de este nodo, arranca siendo None
