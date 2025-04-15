import time
import random




def ordenamiento_burbuja(lista):           
    n = len(lista)                        
    
    for i in range(n):                                    
        for j in range(0, n-i-1):                        
            if lista[j] > lista[j+1]:
                num_auxiliar = lista[j]                   
                lista[j] = lista[j+1]
                lista [j+1] = num_auxiliar     
    return lista

def ordenamiento_quicksort(lista):
    if len(lista) <= 1: 
        return lista
    else:
        pivote = lista[len(lista)-1] 
        lista_derecha = [] 
        lista_izquierda = [] 
        lista_numero_igual_que_el_pivote = []
    
        for i in lista: 
            if i < pivote:
                lista_izquierda.append(i) 
            elif i == pivote:
                lista_numero_igual_que_el_pivote.append(i)
            else:
                lista_derecha.append(i)
    return ordenamiento_quicksort(lista_izquierda) + lista_numero_igual_que_el_pivote + ordenamiento_quicksort(lista_derecha)
    

def counting_sort(lista, exponente_actual):             # el exponente_acutal es el que nos dice con que digito de cada uno de los numeros estamos trabajando
    lista_auxiliar = [0] * len(lista)                   # La lista_auxiliar es una lista que posee la misma longitud que la lista original (si la lista tiene 23 elementos, esta posee 23 elementos tambien). Esta lista nos sirve para llevar el ordenamiento de la lista digito por digito a medida que avanzamos sin modificar la lista original
    lista_conteo = [0] * 10                             # Esta lista tiene 10 espacios ya que los valores de los numeros que nos pueden aparecer en cada digito van de 0-9. se encarga de contar la cantidad de veces que aparece cada digito, sumando 1 en el valor de su casilla por cada vez que aparece

    for numero in lista:
        indice = numero // exponente_actual             # El numero es el numero que esamos procesando dentro de la lista, y el exponente actual nos indica el valor de la posicion del digito que estamos ordenando (si el numero es, 187 y el exponente es 1, entonces al hacerle % 10 el digito que queda como residuo es el 7, si el exponente es 10, entonces el digito que queda como residuo es es el 8, si exponente es 100 entonces el digito es el 1) # Recordemos que lo que hace "//" es una division entera en la que se descarta la parte desimal
        lista_conteo[indice % 10] += 1                  # Lo que el operador % 10 hace es dividir entre 10 el numero y luego quedarnos con el resto (es decir que si indice = 187 entonces indice % 10 = 7. si indice = 18 entonces indice % 10 = 8 y asi sucesivamente)
                                                        # Por lo tanto, lo que basicamente estamos haciendo es decirle al programa "aumenta en 1 el valor de la lista de conteo en la posicion numero"
    for i in range (1, 10):                             # Este ciclo va desde i=1 hasta i=10 y lo que hace es
        lista_conteo[i] += lista_conteo[i-1]            # Lo que hace aca es sumar acumulativamente los valores de los espacios anteriores, es decir. si en un inicio Lista_conteo = [0,1,0,1,0,4,2,0,2], al terminar el ciclo va a terminar quedando lista_conteo = [0,1,1,2,2,6,8,8,10] ya que el proceso interno que se lleva a cabo es: [0, (1+0), (0+1), (1+1), (0+2), (4+2), (2+6), (0+8), (2+8)]

    i = len(lista) -1                                   # Necesitamos recorrer todos los espacios de la lista para volver a armarla, por lo que establecemos a j como el ultimo indice de la lista (osea, que si la lista tiene 14 elementos, i=13, que es el indice del ultimo elemento, ya que el elemento 14 se encuentra en el espacio 13)
    while i >= 0:                                       #En este ciclo while vamos a reconstruir la lista, esta vez ya ordenada (o parcialmente ordenada, dependiendo de cuantos exponentes nos falten recorrer) recorriendo de derecha a izquierda, por eso llegamos hasta el valor 0 inclusive
        num_actual = lista[i]                           # El numero actual que estamos procesando
        indice = num_actual // exponente_actual             #Estamos haciendo lo mismo que en la linea 37
        lista_auxiliar[lista_conteo[indice % 10]-1] = num_actual
        lista_conteo[indice % 10] -= 1                      #Le restamos uno al valor que es encuentra en dicho espacio, ya que ahora hay uno menos (por que ya lo colocamos en la lista)
        i -= 1                                  # Vamos reduciendo i en 1 para que asi trabaje con otros valores de la lista

    for i in range(len(lista)):
        lista[i] = lista_auxiliar[i]            #Ahora si, actualizamos los valores de la lista original que nos enviaron


def ordenamiento_por_residuos(lista):
    if len(lista) <= 1:                         #en caso de que la funcion este vacia o tenga un solo elemento (en cuyo caso no habria nada que ordenar)
        return lista
    
    numero_maximo = max(lista)
    exponente = 1                               # Inicializamos el exponente en 1, para que trabaje con unidades, y que posteriormente pase a decenas, centenas, etc.
    
    
    while numero_maximo // exponente > 0:       # Mientras que sigan quedando exponentes que trabajar, segui llamando a la funcion (ya que en el momento en el que no queden, si por ejemplo numero_maximo= 58 y exponente= 100 entonces numero_maximo // exponente sera < 0)
        counting_sort(lista, exponente)
        exponente *= 10                         # Multiplica el exponente por 10 despues de cada llamada a la funcion counting_sort
    return lista


#A PARTIR DE ACA VOY A RESOLVER LA ACTIVIDAD 2, DESPUES VERE EN QUE CARPETA LO METO

def medir_tiempo(algoritmo, lista):
    tiempo_inicial = time.time()            #aca establecemos el tiempo en t=0
    algoritmo(lista)                        #aca llamamos al algoritmo en cuestion al que queremos tomarle el tiempo y le enviamos la lista
    tiempo_final = time.time()              #aca dejamos de correr el tiempo, ya que la funcion ya actuo
    tiempo_transcurrido = tiempo_final-tiempo_inicial
    return tiempo_transcurrido              #finalmente, nos devuelve el tiempo que tardo en total


tamanios_listas = [1, 10, 100, 500, 1000]   #estos son los tamaños de lista que queremos medir, listas con 1, 10, 100, 500 y 1000 elementos
tiempos_ordenamiento_burbuja = []   
tiempos_ordenamiento_quicksort = []         #en estas tres listas almacenamos los tiempos corres´pondientes a cada uno de los tamaños (es decir que las listas van a tener 5 elementos c/u)
tiempos_ordenamiento_radixsort = []

for i in tamanios_listas:
    lista_aleatoria = []






if __name__ == "__main__":

    lista1 = [1, 112, 8, 100, 434, 23, 86, 13]
    lista1_ordenada = ordenamiento_burbuja(lista1)
    print(lista1_ordenada)

    lista2 = [1, 3, 5, 45, 29849, 187, 3, 170, 44, 18821, 86, 13, 13, 892]
    lista2_ordenada = ordenamiento_quicksort(lista2)
    print(lista2_ordenada)

    lista3 = [1, 82, 5, 7127, 249, 17, 34, 127, 44, 1821, 86, 1187, 13, 82, 88, 44]
    lista3_ordenada = ordenamiento_por_residuos(lista3)
    print(lista3_ordenada)