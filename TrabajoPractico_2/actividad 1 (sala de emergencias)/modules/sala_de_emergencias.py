import time
import datetime
import modules.paciente as pac
import random
from modules.cola_prioridad import ColaPrioridad

n = 20  # cantidad de ciclos de simulación

cola_de_espera = ColaPrioridad()                                            #Aca antes habia un "cola_de_espera = list()", lo cambie por que sino no puedo usar la cola de prioridad

# Ciclo que gestiona la simulación
for i in range(n):                                                          #No toco nada, esto esta bien asi
    # Fecha y hora de entrada de un paciente
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*15)
    print('\n', fecha_y_hora, '\n')

    # Se crea un paciente un paciente por segundo
    # La criticidad del paciente es aleatoria
    paciente = pac.Paciente()                                               
    prioridad = (paciente.get_riesgo(), paciente.get_fecha_llegada())       #Estos dos valores los voy a usar para determinar que tan prioritario es atender a un paciente, basandome en que tan critico esta (paciente.get_riesgo()) y basandome en cuando llego (paciente.get_fecha_llegada())
    cola_de_espera.agregar_paciente((prioridad, paciente))                  #Y aca es donde finalmente agrego al paciente a la cola de prioridad, 

    # Atención de paciente en este ciclo: en el 50% de los casos
    if random.random() < 0.5:
        # se atiende paciente que se encuentra al frente de la cola
        _, paciente_atendido = cola_de_espera.quitar_paciente()             #Aca antes habia un "paciente_atendido = cola_de_espera.pop(0)" que basicamente quitaba el ultimo elemento de la lista,
        print('*'*40)
        print('Se atiende el paciente:', paciente_atendido)
        
        print('*'*40)
    else:
        # se continúa atendiendo paciente de ciclo anterior
        pass
    
    print()

    # Se muestran los pacientes restantes en la cola de espera
    print('Pacientes que faltan atenderse:', len(cola_de_espera))
    for _, paciente in cola_de_espera.elementos:
        print('\t', paciente)
    
    print()
    print('-*-'*15)
    
    time.sleep(1)
