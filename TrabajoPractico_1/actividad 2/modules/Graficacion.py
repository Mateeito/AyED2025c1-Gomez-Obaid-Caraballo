from modules.LDE import ListaDobleEnlazada
import matplotlib.pyplot as pyplo
import time


def medir_tiempo(func, *args):
        inicio = time.perf_counter()                #establece el inicio del tiempo t=0
        func(*args)                                 #ejecuta la funcion que se le pase como argumento
        return time.perf_counter() - inicio         #

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
