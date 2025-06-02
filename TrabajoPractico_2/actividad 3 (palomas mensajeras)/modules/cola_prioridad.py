from modules.monticulo import MonticuloBinario

class ColaPrioridad:
    def __init__(self):
        self.monticulo = MonticuloBinario()

    def insertar(self, vertice):
        self.monticulo.insertar(vertice)

    def eliminar_min(self):
        return self.monticulo.eliminar_min()

    def construir_monticulo(self, lista):
        self.monticulo.construir_monticulo(lista)

    def esta_vacio(self):
        return self.monticulo.esta_vacio()

    def actualizar_distancia(self, vertice, nueva_distancia):
        self.monticulo.actualizar_distancia(vertice, nueva_distancia)
