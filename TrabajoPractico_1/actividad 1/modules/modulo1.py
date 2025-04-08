
def ordenamiento_burbuja(lista):           
    n = len(lista)                        
    
    for i in range(n):                                    
        for j in range(0, n-i-1):                        
            if lista[j] > lista[j+1]:
                num_auxiliar = lista[j]                   
                lista[j] = lista[j+1]
                lista [j+1] = num_auxiliar     
    return lista

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
    


def ordenamiento_por_residuos():
    pass





if __name__ == "__main__":

    lista1 = [1, 112, 8, 100, 434, 23, 86, 13]
    lista1_ordenada = ordenamiento_burbuja(lista1)
    print(lista1_ordenada)

    lista2 = [1, 3, 5, 45, 29849, 187, 3, 170, 44, 18821, 86, 13, 13, 892]
    lista2_ordenada = ordenamiento_quicksort(lista2)
    print(lista2_ordenada)

    lista3 = [1, 8, 5, 77, 249, 17, 3, 127, 44, 18821, 86, 13, 13, 82]
    lista3_ordenada = ordenamiento_quicksort(lista3)
    print(lista3_ordenada)