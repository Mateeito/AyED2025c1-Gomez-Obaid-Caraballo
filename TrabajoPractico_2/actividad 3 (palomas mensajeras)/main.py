from modules.grafo import cargar_grafo
from modules.algoritmo_prim import prim, calcular_sumas_distancias

def imprimir_recorrido_mst(mst, inicio):
    visitados = set()
    cola = [(inicio, None)]
    visitados.add(inicio)

    print("Recorrido:")
    while cola:
        actual, predecesor = cola.pop(0)
        if predecesor is None:
            print(f"- {actual} es la aldea de inicio.")
        else:
            print(f"- {predecesor} envía la noticia a {actual}.")

        for vecino in [aldea for aldea, pred in mst.items() if pred and pred.nombre == actual and aldea not in visitados]:
            cola.append((vecino, actual))
            visitados.add(vecino)

def mostrar_aldeas_alfabeticamente(grafo):
    aldeas_ordenadas = sorted(grafo.vertices.keys())
    print("Aldeas ordenadas:")
    for aldea in aldeas_ordenadas:
        print(f"- {aldea}")

def main():
    grafo = cargar_grafo("data/aldeas.txt")
    aldea_inicio = "Peligros"
    mst = prim(grafo, aldea_inicio)
    suma_distancias, suma_total = calcular_sumas_distancias(grafo, mst)

    while True:
        print("\n")
        print("1. Lista de aldeas en orden alfabético")
        print("2. Distancias de cada aldea a su predecesor")
        print("3. Recorrido del mensaje")
        print("4. Salir")

        opcion = input("Elegí una opción: ").strip()


        if opcion == "1":
            mostrar_aldeas_alfabeticamente(grafo)
        elif opcion == "2":
            print("Distancias por aldea:")
            for aldea, distancia in suma_distancias.items():
                print(f"- {aldea} ← {mst[aldea].nombre} : {distancia}")
            print(f"Total de distancias: {suma_total}")
        elif opcion == "3":
            imprimir_recorrido_mst(mst, aldea_inicio)
        elif opcion == "4":
            print("¡Chau!")
            break
        else:
            print("Opción inválida, probá de nuevo.")

if __name__ == "__main__":
    main()

