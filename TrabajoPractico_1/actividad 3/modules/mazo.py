from modules.LDE import ListaDobleEnlazada 

class DequeEmptyError(Exception):
    def __init__(self, mensaje="oopps, el mazo esta vacio."):
        super().__init__(mensaje)  #se lanza la excepcion 

class Mazo:
    def __init__(self):
        self._cartas = ListaDobleEnlazada()  #se crea el mazo como una lista doble enlazada

    def poner_carta_arriba(self, carta):
        """Agrega una carta al principio del mazo."""
        self._cartas.agregar_al_inicio(carta)

    def poner_carta_abajo(self, carta):
        """Agrega una carta al final del mazo."""
        self._cartas.agregar_al_final(carta)

    def sacar_carta_arriba(self, mostrar=False):
        """Saca la carta del principio del mazo. Lanza DequeEmptyError si está vacío."""
        if self.esta_vacio():
            raise DequeEmptyError()
        carta = self._cartas.extraer(0)
 
        if mostrar:
            carta.visible = True
        else:
            carta.visible = False
        return carta

    def esta_vacio(self):
        """Devuelve True si el mazo está vacío."""
        return len(self._cartas) == 0

    def __len__(self):
        """Devuelve la cantidad de cartas en el mazo."""
        return len(self._cartas)

    def __str__(self):
        """Devuelve una representación en cadena del mazo."""
        return str(self._cartas)

    def __repr__(self):
        return self.__str__()