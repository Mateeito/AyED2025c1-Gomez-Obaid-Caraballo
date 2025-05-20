import random       

class Paciente:
    def __init__(self):
        self.nombre = f'Paciente{random.randint(100, 999)}' 
        self.riesgo = random.randint(1, 3)                  
    
    
    def __repr__(self):
        niveles = {1: 'Crítico', 2: 'Moderado', 3: 'Bajo'}      
        return f'{self.nombre} (Riesgo: {niveles[self.riesgo]})'  