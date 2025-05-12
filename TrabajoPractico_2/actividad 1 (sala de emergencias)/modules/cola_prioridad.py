import heapq    # Este módulo implementa un montículo (heap), una estructura de datos que se comporta como un árbol binario completo y mantiene el orden de prioridad.


class ColaPrioridad:
    def __init__(self):
        self.cola = []                          #Inicializamos con una lista vacia a la que llamaremos "cola" por que es una "cola de personas" osea una fila de personas esperando a ser atendidas
        self.contador = 0                       #Para mantener el orden de llegada, este contador se incrementará cada vez que se inserte un elemento, permitiendo que dos elementos con igual prioridad se ordenen según quién llegó primero

    def insertar(self, prioridad, paciente):    #Cuanto menor es la prioridad, más urgente es (nivel de riesgo, de modo que 1 > 2 > 3 en cuanto a prioridad)
        heapq.heappush(self.cola, (prioridad, self.contador, paciente)) #Voy a explicar lo que hace "heapq.heappush(lista, elemento)" para que se entienda bien. Lo que hace es que inserta un "elemento" en el monticulo, este "elemento" en este caso es una tupla con los valores (prioridad, contador, nombre_paciente). y para decidir en que posicion de la cola va a ir este elemento, internamiente lo que heappush hace es comparar inmediatamente el nuevo elemento con los que ya se encuentran en la cola. Por lo que una vez ejecutada la funcion matamos dos pajaros de un tiro, por que agregamos el elemento con sus respectivos valores, y ademas ya lo dejamos en su posicion correcta de prioridad dentro de la cola
    #Nota: podriamos insertar el elemento en su posicion correcta comparando cada elemento con los demas usando un condicional, pero es mucho mas facil asi como lo estoy haciendo.                                                                                                                                                                                                                                                                                                                                                                                                                                                             prioridad,llegada
    #Nota 2: La forma en la que internamente la funcion heappush compara los valores de la tupla es la siguiente: compara el primer valor de la tupla del nuevo "elemento" (en este caso seria la "prioridad") con las demas "prioridades" de los demas "elementos" de la cola y posiciona ese elemento segun su valor (por ej: si prioridad=2, y cola=[1,1,3,3,3] entonces va a quedar cola=[1,1,2,3,3,3] ), y en caso de que se encuentre un valor igual de "prioridad" lo que hace es pasar al siguiente valor del "elemento" (en este caso seria el "contador" que viene a ser su orden de llegada) y lo coloca en la cola (es decir, si elemento= (1,3) y cola = [(1,2) , (1,4) , (2,1) , (2,6) , (3,5)] entonces quedaria cola = [(1,2) , (1,3) , (1,4) , (2,1) , (2,6) , (3,5)]).   
        self.contador += 1                      #Incrementa el contador para el proximo elemento que se inserte

    def extraer(self):
        if self.cola:                           #Este if verifica que la lista no este vacia, devolviendo un valor booleano. Recordemos que, como la cola ya se encuentra ordenada, no es necesaria ninguna verificacion previa, y podemos pasar a extraer el primer valor disponible (que en este caso seria el de mayor prioridad). 
            return heapq.heappop(self.cola)[2]  #Devolvemos solo el elemento [2] de los datos del paciente, es decir, su "nombre". Ya que recordemos que el paciente tiene 3 datos: (prioridad, posicion en el contador, nombre del paciente), por lo que baicamente le estamos diciendo al programa "saca al paciente mas urgente de la lista (presuntamente para atenderlo) y decime cual es su nombre, no es necesario que me digas la prioridad ni el orden de llegada"
        else:
            return None                         #En caso de que la lista este vacia, que no devuelva nada

    def esta_vacia(self):
        if len(self.cola) == 0:
            return True             #Retorna True si no hay elementos en la lista
        else:
            return False            #Retorna False si hay al menos un elemento en la lista

    def __len__(self):              #Permite usar la función len() sobre la cola de prioridad.
        return len(self.cola)       #Retorna la cantidad de elementos (pacientes) que hay en la cola.

    def __iter__(self):
        return (item[2] for item in sorted(self.cola)) #Devuelve solo el nombre de los pacientes (último elemento de cada tupla), sin mostrar la prioridad ni el contador.
    