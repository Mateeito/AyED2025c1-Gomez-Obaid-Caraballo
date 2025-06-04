import sys

class Vertice:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__conexiones = {}
        self.__distancia = sys.maxsize
        self.__predecesor = None

    def agregar_conexion(self, vertice, ponderacion):
        self.__conexiones[vertice] = ponderacion

    def obtener_conexiones(self):
        return self.__conexiones.keys()

    def obtener_ponderacion(self, vertice):
        return self.__conexiones[vertice]

    @property
    def distancia(self):
        return self.__distancia

    @distancia.setter
    def distancia(self, dist):
        self.__distancia = dist

    @property
    def predecesor(self):
        return self.__predecesor

    @predecesor.setter
    def predecesor(self, predecesor):
        self.__predecesor = predecesor

    @property
    def nombre(self):
        return self.__nombre

class Grafo:
    def __init__(self):
        self.__vertices = {}

    def agregar_vertice(self, nombre):
        vertice = Vertice(nombre)
        self.__vertices[nombre] = vertice
        return vertice

    def obtener_vertice(self, nombre):
        return self.__vertices.get(nombre, None)

    def agregar_arista(self, desde, hasta, peso):
        if desde not in self.__vertices:
            self.agregar_vertice(desde)
        if hasta not in self.__vertices:
            self.agregar_vertice(hasta)
        self.__vertices[desde].agregar_conexion(self.__vertices[hasta], peso)
        self.__vertices[hasta].agregar_conexion(self.__vertices[desde], peso)

    @property
    def vertices(self):
        return self.__vertices

def cargar_grafo(desde_archivo):
    grafo = Grafo()
    with open(desde_archivo, 'r') as archivo:
        for linea in archivo:
            datos = linea.strip().split(', ')
            if len(datos) == 3:
                desde, hasta, distancia = datos
                grafo.agregar_arista(desde, hasta, int(distancia))
    return grafo
