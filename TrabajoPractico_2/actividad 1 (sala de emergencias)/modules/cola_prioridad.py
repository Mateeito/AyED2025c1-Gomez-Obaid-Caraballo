
class ColaPrioridad:
    def __init__(self):
        self.elementos = []

    def __len__(self):
        return len(self.elementos)

    def _subir(self, posicion):
        while posicion > 0:
            posicion_padre = (posicion - 1) // 2
            if self._es_menor(posicion, posicion_padre):
                self._intercambiar(posicion, posicion_padre)
                posicion = posicion_padre
            else:
                break

    def _bajar(self, posicion):
        tamanio = len(self.elementos)
        while True:
            posicion_menor = posicion
            hijo_izq = 2 * posicion + 1
            hijo_der = 2 * posicion + 2

            if (hijo_izq < tamanio and self._es_menor(hijo_izq, posicion_menor)):
                posicion_menor = hijo_izq

            if (hijo_der < tamanio and self._es_menor(hijo_der, posicion_menor)):
                posicion_menor = hijo_der

            if posicion_menor == posicion:
                break

            self._intercambiar(posicion, posicion_menor)
            posicion = posicion_menor

    def _es_menor(self, i, j):
        # Compara las claves de prioridad de los elementos
        prioridad_i = self.elementos[i][0]
        prioridad_j = self.elementos[j][0]
        return prioridad_i < prioridad_j

    def _intercambiar(self, i, j):
        self.elementos[i], self.elementos[j] = self.elementos[j], self.elementos[i]

    def agregar_paciente(self, nuevo_elemento):
        self.elementos.append(nuevo_elemento)
        self._subir(len(self.elementos) - 1)

    def quitar_paciente(self):
        if len(self.elementos) == 0:
            raise IndexError("La cola de prioridad está vacía")
        
        self._intercambiar(0, len(self.elementos) - 1)
        elemento_prioritario = self.elementos.pop()

        if len(self.elementos) > 0:
            self._bajar(0)
            
        return elemento_prioritario

 