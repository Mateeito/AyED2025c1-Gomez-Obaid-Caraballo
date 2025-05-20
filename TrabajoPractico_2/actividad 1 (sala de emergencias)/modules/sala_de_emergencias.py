import random
import time
import datetime
from modules.cola_prioridad import ColaPrioridad
from modules.paciente import Paciente

if __name__ == "__main__":

    n = 20                                  
    cola_de_espera = ColaPrioridad()        

    for i in range(n):                      
        ahora = datetime.datetime.now()     
        fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S') 
        print('-*-'*15)                     
        print('\n', fecha_y_hora, '\n')     

        nuevo_paciente = Paciente()               
        cola_de_espera.insertar(nuevo_paciente.riesgo, nuevo_paciente)  

        if random.random() < 0.5 and not cola_de_espera.esta_vacia():   
            paciente_atendido = cola_de_espera.extraer()                
            print('*'*40)                                               
            print('Se atiende el paciente:', paciente_atendido)         
            print('*'*40)                                               
        else:                                                           
            pass

        print('Pacientes que faltan atenderse:', len(cola_de_espera))   
        for paciente in cola_de_espera:
            print('\t', paciente)
    
        print()         
        print('-*-'*15) 
        time.sleep(1)   
