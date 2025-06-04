import sys
from modules.cola_prioridad import ColaPrioridad

def prim(grafo, inicio_nombre):
    inicio = grafo.obtener_vertice(inicio_nombre)
    if not inicio:
        raise ValueError("La aldea de inicio no existe en el grafo")

    cp = ColaPrioridad()
    for vertice in grafo.vertices.values():
        vertice.distancia = sys.maxsize
        vertice.predecesor = None
    inicio.distancia = 0

    cp.construir_monticulo(list(grafo.vertices.values()))

    while not cp.esta_vacio():
        vertice_actual = cp.eliminar_min()
        for vecino in vertice_actual.obtener_conexiones():
            nuevo_costo = vertice_actual.obtener_ponderacion(vecino)
            if vecino.distancia > nuevo_costo and vecino != vertice_actual.predecesor:
                vecino.distancia = nuevo_costo
                vecino.predecesor = vertice_actual
                cp.actualizar_distancia(vecino, nuevo_costo)

    return {vertice.nombre: vertice.predecesor for vertice in grafo.vertices.values()}

def calcular_sumas_distancias(grafo, mst):
    suma_distancias = {}
    for aldea, predecesor in mst.items():
        if predecesor:
            distancia = grafo.obtener_vertice(predecesor.nombre).obtener_ponderacion(grafo.obtener_vertice(aldea))
            suma_distancias[aldea] = distancia
    total_suma = sum(suma_distancias.values())
    return suma_distancias, total_suma
