def ordenamiento_quicksort(lista):
    if len(lista) <= 1: 
        return lista
    else:
        pivote = lista[len(lista)-1] 
        lista_derecha = [] 
        lista_izquierda = [] 
        lista_numero_igual_que_el_pivote = []
    
        for i in lista: 
            if i < pivote:
                lista_izquierda.append(i) 
            elif i == pivote:
                lista_numero_igual_que_el_pivote.append(i)
            else:
                lista_derecha.append(i)
    return ordenamiento_quicksort(lista_izquierda) + lista_numero_igual_que_el_pivote + ordenamiento_quicksort(lista_derecha)
    
if __name__ == "__main__":

    lista2 = [1, 3, 5, 45, 29849, 187, 3, 170, 44, 18821, 86, 13, 13, 892]
    lista2_ordenada = ordenamiento_quicksort(lista2)
    print(lista2_ordenada)