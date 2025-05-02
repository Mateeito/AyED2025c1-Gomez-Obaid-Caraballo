
import time
import random
from modules.ordenamiento_burbuja import ordenamiento_burbuja
from modules.ordenamiento_quicksort import ordenamiento_quicksort
from modules.ordenamiento_por_residuos import ordenamiento_por_residuos

def medir_tiempo(algoritmo, lista):
    tiempo_inicial = time.perf_counter()        #aca establecemos el tiempo en t=0
    algoritmo(lista)                        #aca llamamos al algoritmo en cuestion al que queremos tomarle el tiempo y le enviamos la lista
    tiempo_final = time.perf_counter()             #aca dejamos de correr el tiempo, ya que la funcion ya actuo
    tiempo_transcurrido = tiempo_final-tiempo_inicial
    return tiempo_transcurrido              #finalmente, nos devuelve el tiempo que tardo en total

