class Carta:
    
    def __init__(self, valor='', palo=''):
        self.valor = valor
        self.palo = palo
        self.visible:bool = False
        
    @property
    def visible(self): 
        return self._visible 
        
    @visible.setter  #dice si la carta tiene que mostrarse o no
    def visible(self, visible):   #si es falso la carta sale como "-x"
        self._visible = visible
        
    @property
    def valor(self):  #obtiene el valor de la carta
        return self._valor
    
    @valor.setter
    def valor(self, valor): #asigna el valor de la carta
        self._valor = valor
        
    @property
    def palo(self):
        return self._palo   #obtiene el palo de la carta
    
    @palo.setter
    def palo(self, palo):
        self._palo = palo  
    
    def _valor_numerico(self):
        valores = ['J','Q','K','A']  #le asigna un valor numerico a las letras
        if self.valor in valores:
            idx = valores.index(self.valor)
            return (11 + idx)
        return int(self.valor)            
            
        
    def __gt__(self, otra):
        """2 cartas deben compararse por su valor numérico"""
        return self._valor_numerico() > otra._valor_numerico() #compara los valores de las cartas
        
    def __str__(self):
        if self.visible == False: 
            return "-X"
        else:
            return self.valor + self.palo
    
    def __repr__(self): 
        return str(self) 
    
    
if __name__ == "__main__": 
    carta = Carta("3", "♣")
    print(carta)
    carta.visible = True
    print(carta)
    