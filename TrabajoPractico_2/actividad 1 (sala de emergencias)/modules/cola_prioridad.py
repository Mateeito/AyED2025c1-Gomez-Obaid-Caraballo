import heapq    


class ColaPrioridad:
    def __init__(self):
        self.cola = []                          
        self.contador = 0                       

    def insertar(self, prioridad, paciente):    
        heapq.heappush(self.cola, (prioridad, self.contador, paciente)) 
        self.contador += 1                      

    def extraer(self):
        if self.cola:                           
            return heapq.heappop(self.cola)[2]  
        else:
            return None                         

    def esta_vacia(self):
        if len(self.cola) == 0:
            return True             
        else:
            return False           

    def __len__(self):              
        return len(self.cola)       
    def __iter__(self):
        return (item[2] for item in sorted(self.cola))  