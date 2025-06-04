class Grafo:
    def __init__(self):
        self.adyacencias = {}  # Diccionario común

    def agregar_arista(self, origen, destino, peso):
        if origen not in self.adyacencias:
            self.adyacencias[origen] = []
        if destino not in self.adyacencias:
            self.adyacencias[destino] = []
        self.adyacencias[origen].append((destino, peso))
        self.adyacencias[destino].append((origen, peso))  # Grafo no dirigido

    def obtener_adyacentes(self, nodo):
        return self.adyacencias.get(nodo, [])

    def obtener_nodos(self):
        return list(self.adyacencias.keys())
    
    