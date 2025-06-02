import math

class MonticuloBinario:
    def __init__(self):
        self.__lista_monticulo = [-math.inf]
        self.__tamano_actual = 0

    def _infilt_arriba(self, i):
        while i // 2 > 0:
            if self.__lista_monticulo[i].distancia < self.__lista_monticulo[i // 2].distancia:
                self.__lista_monticulo[i], self.__lista_monticulo[i // 2] = self.__lista_monticulo[i // 2], self.__lista_monticulo[i]
            i = i // 2

    def insertar(self, vertice):
        self.__lista_monticulo.append(vertice)
        self.__tamano_actual += 1
        self._infilt_arriba(self.__tamano_actual)

    def _infilt_abajo(self, i):
        while (i * 2) <= self.__tamano_actual:
            hm = self._hijo_min(i)
            if self.__lista_monticulo[i].distancia > self.__lista_monticulo[hm].distancia:
                self.__lista_monticulo[i], self.__lista_monticulo[hm] = self.__lista_monticulo[hm], self.__lista_monticulo[i]
            i = hm

    def _hijo_min(self, i):
        if i * 2 + 1 > self.__tamano_actual:
            return i * 2
        else:
            return i * 2 if self.__lista_monticulo[i * 2].distancia < self.__lista_monticulo[i * 2 + 1].distancia else i * 2 + 1

    def eliminar_min(self):
        if self.esta_vacio():
            raise ValueError("El montículo está vacío.")
        valor_sacado = self.__lista_monticulo[1]
        self.__lista_monticulo[1] = self.__lista_monticulo[self.__tamano_actual]
        self.__tamano_actual -= 1
        self.__lista_monticulo.pop()
        self._infilt_abajo(1)
        return valor_sacado

    def construir_monticulo(self, lista):
        self.__tamano_actual = len(lista)
        self.__lista_monticulo = [0] + lista[:]
        for i in range(self.__tamano_actual // 2, 0, -1):
            self._infilt_abajo(i)

    def esta_vacio(self):
        return self.__tamano_actual == 0

    def actualizar_distancia(self, vertice, nueva_distancia):
        for i in range(1, self.__tamano_actual + 1):
            if self.__lista_monticulo[i] == vertice:
                vertice.distancia = nueva_distancia
                self._infilt_arriba(i)
                break
