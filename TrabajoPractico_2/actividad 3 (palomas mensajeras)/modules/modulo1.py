import heapq
from modules import grafo 

# Función para leer el archivo y construir el grafo
def leer_archivo(nombre_archivo):
    g = grafo.Grafo()  # Accedés a la clase Grafo desde el módulo
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            origen, destino, distancia = linea.strip().split(",")
            distancia = int(distancia)
            g.agregar_arista(origen, destino, distancia)
    return g

# Algoritmo de Prim para encontrar el árbol de expansión mínima
def prim(grafo_obj, inicio):
    visitado = set()
    heap = [(0, inicio, None)]  # (peso, nodo_actual, nodo_origen)
    mst = {}  # nodo_actual: (nodo_origen, peso)
    total = 0

    while heap:
        peso, actual, origen = heapq.heappop(heap)
        if actual in visitado:
            continue
        visitado.add(actual)
        if origen:
            mst[actual] = (origen, peso)
            total += peso
        for vecino, peso_vecino in grafo_obj.obtener_adyacentes(actual):
            if vecino not in visitado:
                heapq.heappush(heap, (peso_vecino, vecino, actual))
    return mst, total

# Construye los reenvíos para mostrar quién informa a quién
def construir_reenvios(mst):
    hijos = {}
    for nodo, (padre, _) in mst.items():
        if padre not in hijos:
            hijos[padre] = []
        hijos[padre].append(nodo)
    return hijos

# Muestra todos los resultados
def mostrar_resultados(grafo_obj, mst, total, inicio):
    aldeas = sorted(grafo_obj.obtener_nodos())
    print("Lista de aldeas en orden alfabético:")
    for aldea in aldeas:
        print(f"- {aldea}")

    print("\nDistribución del mensaje:")
    hijos = construir_reenvios(mst)
    for aldea in aldeas:
        if aldea == inicio:
            print(f"\n{aldea} (origen):")
        else:
            padre, peso = mst[aldea]
            print(f"\n{aldea}:")
            print(f"  Recibe la noticia de: {padre} ({peso} leguas)")
        if hijos.get(aldea):
            destinos = ", ".join(sorted(hijos[aldea]))
            print(f"  Envía la noticia a: {destinos}")
        else:
            print(f"  No reenvía la noticia.")
    print(f"\nDistancia total recorrida por todas las palomas: {total} leguas")

# Función principal
def main():
    grafo_obj = leer_archivo("aldeas.txt")
    inicio = "Peligros"
    mst, total = prim(grafo_obj, inicio)
    mostrar_resultados(grafo_obj, mst, total, inicio)

if __name__ == "__main__":
    main()