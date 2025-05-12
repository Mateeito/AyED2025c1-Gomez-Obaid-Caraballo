import random
import time
import datetime
from modules.cola_prioridad import ColaPrioridad
from modules.paciente import Paciente

if __name__ == "__main__":

    n = 20                                  #Cantidad de ciclos de simulación
    cola_de_espera = ColaPrioridad()        #Creo un objeto tipo ColaPrioridad

    for i in range(n):                      #Hago un bucle para los n ciclos (en este caso me voy a basar en el codigo brindado por la catedra y voy a poner n=20)
        ahora = datetime.datetime.now()     #Tomo la fecha y tiempo actual
        fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S') #Esta línea convierte el objeto "ahora" en una cadena de texto con formato legible (%d = dia , %m = mes , %y = año // %H = hora, %M = minutos, %S = segundos)
        print('-*-'*15)                     #Esta linea imprime una lista decorativa, solamente sirve para hacer mas clara y linda visualmente la salida por consola
        print('\n', fecha_y_hora, '\n')     #Imprimimos la "fecha y ahora" actual del ciclo, esto va a pasar las n veces que dure el ciclo, para asi poder distinguir claramente en que momento del ciclo estamos

        nuevo_paciente = Paciente()               #En cada ciclo creamos un nuevo paciente
        cola_de_espera.insertar(nuevo_paciente.riesgo, nuevo_paciente)  #Agregamos a la cola el nuevo paciente. El motivo por el cual no envio simplemente el paciente y luego hago paciente.riesgo para obtener su riesgo es por que, haciendolo de esta forma (pasando solamente paciente) tendria que hacer "from modules.paciente import Paciente" en el modulo de cola_prioridad, y eso seria mas laborioso que simplemente mandar la prioridad

        if random.random() < 0.5 and not cola_de_espera.esta_vacia():   #Lo que hace este if es que, existe una chance del 50% (random.random() < 0.5) de que se atienda a un paciente en este ciclo (esto tiene que ser asi por que, si encada ciclo se atendiera a un paciente, el tamaño de la lista jamas aumentaria). y andemas verifica que la cola no este vacia antes de intertar atender a un paciente (not cola_de_espera.esta_vacia())
            paciente_atendido = cola_de_espera.extraer()                #Extraemos al paciente (que, al estar ya ordenado en la funcion insertar, va a ser siempre el que mas nececidad de ser atendido tenga)
            print('*'*40)                                               #Separacion estetica
            print('Se atiende el paciente:', paciente_atendido)         #Nos dicen a que paciente atendimos (nos da su nombre)
            print('*'*40)                                               #Separacion estetica
        else:                                                           #En caso de que no se cumpla alguna de estas condiciones, que siga de largo nomas
            pass

        print('Pacientes que faltan atenderse:', len(cola_de_espera))   #Esto no se si lo pedian, pero recordando como funciona la sala de espera en lugares como NANI en parana, decidi que iba a quedar mas completo con esto. Pero si los profes nos dicen que es al pedo lo sacamos
        for paciente in cola_de_espera:
            print('\t', paciente)
    
        print()         #imprime un salto de linea (no imprime nada)
        print('-*-'*15) #separacion visual
        time.sleep(1)   #pausa el tiempo de ejecucion del programa durante 1 segundo, para simular el paso de tiempo entre ciclos

