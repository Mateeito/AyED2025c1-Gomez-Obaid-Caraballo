def ordenamiento_burbuja(lista):           
    n = len(lista)                        
    
    for i in range(n):                                    
        for j in range(0, n-i-1):                        
            if lista[j] > lista[j+1]:
                num_auxiliar = lista[j]                   
                lista[j] = lista[j+1]
                lista [j+1] = num_auxiliar     
    return lista

if __name__ == "__main__":
    lista1 = [1, 112, 8, 100, 434, 23, 86, 13]
    lista1_ordenada = ordenamiento_burbuja(lista1)
    print(lista1_ordenada)
