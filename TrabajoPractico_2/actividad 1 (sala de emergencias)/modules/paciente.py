import random       #Lo uso para poder generar un nombre unico al paciente asi como tambien un nivel de riesgo aleatorio entre 1-3

class Paciente:
    def __init__(self):
        self.nombre = f'Paciente{random.randint(100, 999)}' #El nombre del paciente quedaria "Paciente + (numero aleatorio entre 100 y 999)"
        self.riesgo = random.randint(1, 3)                  #Asignamos aleatoriamente entre 1 y 3 su nivel de riesgo, que puede ser 1 (crítico), 2 (moderado) o 3 (bajo)
    #No le asignamos un valor "de llegada" por que eso se asigna una vez que esta en la lista de la "Cola de prioridad"
    
    def __repr__(self):
        niveles = {1: 'Crítico', 2: 'Moderado', 3: 'Bajo'}      #Se define un diccionario llamado niveles que asocia el valor numérico del riesgo con su descripción textual.
        return f'{self.nombre} (Riesgo: {niveles[self.riesgo]})'#Se retorna una cadena formateada que muestra el nombre y el nivel de riesgo del paciente en forma legible.
    