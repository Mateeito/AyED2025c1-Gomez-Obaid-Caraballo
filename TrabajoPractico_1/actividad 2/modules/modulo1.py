import time
import matplotlib.pyplot as pyplo



class Nodo:
    def __init__(self, dato):       #consideremos que, inicialmente, para crear un nodo solo nececitamos saber el valor del propio nodo (el dato)
        self.dato = dato
        self.siguiente = None       #inicialmente el nodo siguiente es None
        self.anterior = None        #inicialmente el nodo anterior es None
    
    def obtenerDato(self):
        return self.dato
    
    def obtenerSiguiente(self):
        return self.siguiente
    
    def obtenerAnterior(self):
        return self.anterior
    
    def asignarDato(self, nuevoDato):
        self.dato = nuevoDato

    def asignarSiguiente(self, nuevodatoSig):
        self.siguiente = nuevodatoSig

    def asignarAnterior(self, nuevodatoAnt):
        self.anterior = nuevodatoAnt


class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self._longitud = 0                                  #ya que, al ser creada iniciamente la lista, esta no posee ninguna longitud ya que aun no posee elementos dentro de ella. Ademas hacemos que sea un atributo privado "_"
  
    def esta_vacia(self):
        return self._longitud == 0                          #lo que hace esta linea es revisar si el atributo longitud es igual a 0, en caso de que este vacia retorna true 

    def __len__(self):
        return self._longitud                               #devuelve la longitud de la lista

    def agregar_al_inicio(self, item):                      #esta funcion coloca el nuevo valor al inicio (cabeza) de la lista
        nodo_a_agregar = Nodo(item)                         #cuando llamamos a la funcion debemos pasarle el valor que queremos que tenga ese nuevo nodo (que en este caso seria el item) y luego creamos un nodo con la clase Nodo. Es decir que si mandamos agregar_al_inicio(8) va a agregar el numero 8 al inicio de la lista
        
        if self.esta_vacia():                               #antes de agregar el nodo a la lista, verifica si la lista esta vacia
            self.cabeza = self.cola = nodo_a_agregar        #en caso de que la lista este vacia (y por lo tanto este nuevo nodo sea el unico elemento) este pasaria a ser tanto la cabeza como la cola
        
        else:
            nodo_a_agregar.siguiente = self.cabeza          #en caso de que la lista NO este vacia, entonces el puntero "siguiente" del nuevo nodo apuntara al valor de la cabeza de la lista (basicamente posicionandose a la izquierda de la cabeza, pasando a ser la nueva cabeza)
            self.cabeza.anterior = nodo_a_agregar           #ahora que la cabeza ya no es mas la cabeza y tiene un nodo anterior (que antes no tenia), tenemos que hacer que el valor anterior de la cabeza (cabeza.anterior) tenga su puntero anterior apuntando hacia la nueva cabeza (nodo_a_agregar)
            self.cabeza = nodo_a_agregar                    #ahora si, hacemos que la nueva cabeza de la lista sea nodo_a_agregar
        
        self._longitud += 1                                 #por ultimo, ya que agregamos un nuevo nodo a la lista, la longitud de la lista incrementa en 1

    def agregar_al_final(self, item):                       #el proceso es parecido a la funcion anterior, pero ahora lo hacemos colocando el nodo en la cola en lugar de en la cabeza
        nodo_a_agregar = Nodo(item)
       
        if self.esta_vacia():
            self.cabeza = self.cola = nodo_a_agregar
        else:
            nodo_a_agregar.anterior = self.cola
            self.cola.siguiente = nodo_a_agregar
            self.cola = nodo_a_agregar
        
        self._longitud += 1

    def insertar(self, item, posicion=None):                #pasamos como argumento el nodo (item) a insertar, y la posicion en la que queremos insertarlo
       
        if posicion is None or posicion == self._longitud:  #esta linea nos dice que, si no se pasa la posicion como argumento (None) o si la posicion corresponde a la longitud total de la lista (es decir al final de la lista) entonces:
            self.agregar_al_final(item)                     #agregamos el nodo al final y listo, y para esto ya tenemos una funcion que hace el trabajo por nosotros
            return                                          #el return hace que la funcion insertar termine
        
        if posicion == 0:                                   #basicamente es lo mismo que agregar un nodo al inicio de la lista, por lo tanto hacemos uso de la funcion agregar_al_inicio:
            self.agregar_al_inicio(item)
            return                                              
        
        if posicion < 0 or posicion > self._longitud:         #si la posicion es un numero negativo o la posicion es mas grande que la propia lista, entonces que nos de un error
            raise IndexError("Posicion NO Valida (fuera de rango)")
        
        #en caso de que no se cumpla ninguno de los anteriores if:
        #                                                                                                                                                                0     1     2     3   
        
        nodo_a_agregar = Nodo(item)                             #para que se entienda todo el siguiente codigo, voy a hacer un ejemplo, supongamos que tenemos la lista [A <-> B <-> C <-> D] y queremos meter el valor 'X' en la posicion 2 (donde esta C) en ese caso:
        actual = self.cabeza                                    #para recorrer la lista, creamos un valor llamado "actual" y nos posicionamos en la cabeza(A). AL DECIR QUE ACTUAL = SELF.CABEZA AUTOMATICAMENTE ESTAMOS DICIENDO QUE ACTUAL ES UN NODO
        
        for _ in range(posicion):                               #el _ sirve para indicarle a python que no nos importa el valor de la variable del bucle, y que solo queremos recorrerla. 
            actual = actual.siguiente                           #recorremos la lista hasta que llegemos a la 'posicion' en la que queremos insertar el valor. con el ejemplo de antes, cuando posicion =2 , entonces 
        
        #este if verifica que no estemos insertando el valor en la posicion = 0. si, ya se, este punto ya esta cubierto en el if de la linea 74, pero ya que el codigo no me esta funcionando, queria asegurarme de que no fuera este el problema
        if actual.anterior is None:                             # aca nos esta diciendo "si "
            nodo_a_agregar.siguiente = actual
            actual.anterior = nodo_a_agregar
            self.cabeza = nodo_a_agregar
        else:
            anterior = actual.anterior
            anterior.siguiente = nodo_a_agregar
            nodo_a_agregar.anterior = anterior
            nodo_a_agregar.siguiente = actual
            actual.anterior = nodo_a_agregar
        self._longitud +=1

#A la hora de extraer un dato tenemos 3 posibilidades, que nos pidan el primer elemento (cabeza), que nos pidan el ultimo elemento (cola) o que nos pidan un elemento entre medio de esos dos

    def extraer(self, posicion=None):

        #Primero descarto los casos en los que se produce error:
        if self.esta_vacia():
            raise IndexError("No hay nada que extraer, la lista esta vacia")
        
        if posicion is None:
            posicion = self._longitud - 1

        if posicion < 0 or posicion >= self._longitud:
            raise IndexError("Posición inválida")
        
        
        #que nos pidan el ultimo elemento
        if posicion == self._longitud-1:            #ya que en caso de que no nos den la posicion tenemos que devolver el ultimo elemento (cola) de la lista, podemos: 
            dato = self.cola.dato                                       #extraemos el dato en la posicion que nos piden (en este caso la final (cola)) para retornarlo al final
            if self._longitud == 1:                                     #en caso de que el tamaño de la lista conste de un unico elemento:
                self.cabeza = self.cola = None                          #que toda la lista quede vacia
            else:
                self.cola = self.cola.anterior                          #en caso de que la lista tenga mas de 1 elemento, que la nueva cola sea el elemento anterior a la antigua cola
                self.cola.siguiente = None
                
            self._longitud -= 1
            return dato
        
        #que nos pidan el primer elemento
        if posicion == 0:
            dato = self.cabeza.dato

            if self._longitud == 1:                                     #mismo proceso que en el caso de arriba
                self.cabeza = self.cola = None
            else:
                self.cabeza = self.cabeza.siguiente
                self.cabeza.anterior = None
            self._longitud -= 1
            return dato
        
        #que nos pidan un elemento entre medio de esos dos

        actual = self.cabeza                                    #voy a explicar este codigo con el mismo ejemplo de lista que use en la funcion insertar (A <-> B <-> C <-> D), supongamos que queremos sacar B
        for _ in range(posicion):       
            actual = actual.siguiente                           #nos posicionamos en B
        
        actual.anterior.siguiente = actual.siguiente            #hacemos que A --> D
        actual.siguiente.anterior = actual.anterior             #hacemos que A <-- D
        self._longitud -= 1             
        return actual.dato                                      #retornamos B
   
    def copiar(self):
        copia = ListaDobleEnlazada()                        #creamos un objeto ListaDoblementeEnlazada
        actual = self.cabeza                                #nos posicionamos en la cabeza de la lista
        while actual is not None:                           #mientras que la lista no se termine:                 
            copia.agregar_al_final(actual.dato)             #agregame al final cada elemento que toque
            actual = actual.siguiente                       #y pasa al siguiente elemento
        return copia                                        #y cuando termines devolveme esa nueva lista


    def invertir(self):                         #lo voy a explicar con el ejemplo de lista de A <-> B <-> C <-> D
        actual = self.cabeza                    #actual= A
        self.cabeza, self.cola = self.cola, self.cabeza # primero hacemos que la cola sea la cabeza y que la cabeza sea la cola, es decir que self.cabeza = D y que self.cola = A
        while actual is not None:
            actual.anterior, actual.siguiente = actual.siguiente, actual.anterior #nos esta diciendo que A.anterior (None) = A.siguiente (B) y que A.siguiente (B) = A.anterior = None
            actual = actual.anterior            #ahora actual (A) = actual.anterior (B)
        #y asi sucesivamente hasta recorrer toda la lista

    def concatenar(self, otra_lista):           #lo que esta funcion hace es concatenar (agregar) los elementos de otra lista al final de la lista actual, sin modificar la otra lista
        copia = otra_lista.copiar()             #primero, hacemos una copia elemento por elemento de la lista que pasamos como argumento, para asi no modificar la lista directamente
        actual = copia.cabeza                   #al igual que en las funciones anteriores, nos posicionamos en la cabeza de la lista antes de empezar a recorrerla
        while actual:                           #mientras siga habiendo nodos en la lista que queremos copiar:
            self.agregar_al_final(actual.dato)  #agregamos nodo por nodo de la otra_lista a la lista propia (self)
            actual = actual.siguiente           #pasamos al nodo siguiente de la otra_lista
        return self
    
    def __add__(self, otra_lista):
        nueva_lista = self.copiar()             #hacemos una copia de la lista propia (self)
        nueva_lista.concatenar(otra_lista)      #a esa copia, le sumamos al final la otra lista
        return nueva_lista                      #retornamos la lista




#a partir de aca medimos los tiempos de ejecucion 
def medir_tiempo(func, *args):
    inicio = time.time()                #establece el inicio del tiempo t=0
    func(*args)                         #ejecuta la funcion que se le pase como argumento
    return time.time() - inicio         #

n_valores = list(range(100, 2100, 200))
tiempos_len = []
tiempos_copiar = []
tiempos_invertir = []

for n in n_valores:
    lista = ListaDobleEnlazada()
    for i in range(n):
        lista.agregar_al_final(i)

    tiempos_len.append(medir_tiempo(len, lista))
    tiempos_copiar.append(medir_tiempo(lista.copiar))
    tiempos_invertir.append(medir_tiempo(lista.invertir))

# Graficar resultados
pyplo.plot(n_valores, tiempos_len, label='len()')
pyplo.plot(n_valores, tiempos_copiar, label='copiar()')
pyplo.plot(n_valores, tiempos_invertir, label='invertir()')
pyplo.xlabel('Cantidad de elementos (N)')
pyplo.ylabel('Tiempo de ejecución (s)')
pyplo.title('Rendimiento de ListaDobleEnlazada')
pyplo.legend()
pyplo.grid(True)
pyplo.show()
