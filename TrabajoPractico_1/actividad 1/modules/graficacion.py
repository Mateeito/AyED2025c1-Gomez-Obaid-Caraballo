
from modules.ordenamiento_burbuja import ordenamiento_burbuja
from modules.ordenamiento_quicksort import ordenamiento_quicksort
from modules.ordenamiento_por_residuos import ordenamiento_por_residuos
from modules.medir_tiempo import medir_tiempo
import time
import matplotlib.pyplot as pyplo   #es el modulo principal de la libreria matplotlib, este nos permite crear graficos
import random



#y ahora si voy a hacer las pruebas de velocidad:
tamaños_listas = [10, 100, 200, 500, 700, 1000]   #estos son los tamaños de lista que queremos medir, listas con 1, 10, 100, 500 y 1000 elementos
#tamaños_listas = range(1, 1001, 10)
tiempos_ordenamiento_burbuja = []   
tiempos_ordenamiento_quicksort = []         #en estas tres listas almacenamos los tiempos corres´pondientes a cada uno de los tamaños (es decir que las listas van a tener 5 elementos c/u)
tiempos_ordenamiento_radixsort = []
tiempos_ordenamiento_sorted = []


for tamaño in tamaños_listas:                                                       #aca, lo que el for hace es basicamente hacer que el proceso de medir el tiempo se repita la misma cantidad de veces que elementos hay en la lista
    lista_aleatoria = [random.randint(10000, 99999) for j in range(tamaño)]        #creamos la lista aleatoria en base a el tamaño que en ese momento toque. cuando tamaño=1 se repetira 1 vez, cuando sea 10 se repetira 10 veces y asi sucesivamente  
    tiempos_ordenamiento_burbuja.append(medir_tiempo(ordenamiento_burbuja, lista_aleatoria)) 
    tiempos_ordenamiento_quicksort.append(medir_tiempo(ordenamiento_quicksort, lista_aleatoria))    #le mandamos la misma lista a los 3 metodos de ordenamiento, y calculamos cuanto tiempo demora cada uno
    tiempos_ordenamiento_radixsort.append(medir_tiempo(ordenamiento_por_residuos, lista_aleatoria))
    tiempos_ordenamiento_sorted.append(medir_tiempo(sorted, lista_aleatoria))
    #ahora, ya se guardan los tiempos en las 3 listas, pero falta graficarlo:

pyplo.figure(figsize=(10,8)) #crea un lienzo de 10 unidade de ancho por 8 unidades de alto

pyplo.plot(tamaños_listas, tiempos_ordenamiento_burbuja, label='Burbuja', color='blue', marker='o') #dibuja una linea con los valores de tamaños_lista en el eje x / dibuja una linea con los tiempos de ejecucion
pyplo.plot(tamaños_listas, tiempos_ordenamiento_quicksort, label='Quicksort', color='red', marker='o')
pyplo.plot(tamaños_listas, tiempos_ordenamiento_radixsort, label='Radix Sort', color='green', marker='o')
pyplo.plot(tamaños_listas, tiempos_ordenamiento_sorted, label='Sorted', color='black', marker='o')


pyplo.xlabel('Tamaño de la lista')      #agrega una etiqueta por debajo del eje x que dice "Tamaño de la lista"
pyplo.ylabel('Tiempo de ejecucion (s)') 
pyplo.legend()
pyplo.grid(True)                        #pone una cuadricula en el fondo
pyplo.show()                            #esto es lo que hace que el grafico se muestre en pantalla