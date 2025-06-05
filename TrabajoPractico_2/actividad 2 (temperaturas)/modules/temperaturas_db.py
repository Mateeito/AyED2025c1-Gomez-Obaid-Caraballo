from datetime import datetime
from modules.nodo_avl import NodoAVL

#Separar el arbol AVL de la base de datos
#

class Temperaturas_DB:
    def __init__(self):
        self.raiz = None    
        self._cantidad = 0  
    
        
    def _altura(self, nodo):    
        if not nodo:        
            return 0            
        else:
            return nodo.altura  


    def _balance(self, nodo):   
        if not nodo:            
            return 0
        else:
            balance = self._altura(nodo.izquierda) - self._altura(nodo.derecha)
            return balance
   
    
    def _rotar_derecha(self, nodo):     
        nodo_iz = nodo.izquierda              
        subarbol_auxiliar = nodo_iz.derecha                  

        nodo_iz.derecha = nodo               
        nodo.izquierda = subarbol_auxiliar             

        nodo.altura = max(self._altura(nodo.izquierda), self._altura(nodo.derecha)) + 1
        nodo_iz.altura = max(self._altura(nodo_iz.izquierda), self._altura(nodo_iz.derecha)) + 1
        return nodo_iz

    def _rotar_izquierda(self, nodo):   
        nodo_der = nodo.derecha                
        subarbol_auxiliar= nodo_der.izquierda              

        nodo_der.izquierda = nodo              
        nodo.derecha = subarbol_auxiliar

        nodo.altura = max(self._altura(nodo.izquierda), self._altura(nodo.derecha)) + 1
        nodo_der.altura = max(self._altura(nodo_der.izquierda), self._altura(nodo_der.derecha)) + 1
        return nodo_der

    def _insertar(self, nodo, fecha, temperatura):
        if not nodo:
            self._cantidad += 1
            return NodoAVL(fecha, temperatura)

        if fecha < nodo.fecha:
            nodo.izquierda = self._insertar(nodo.izquierda, fecha, temperatura)
        elif fecha > nodo.fecha:
            nodo.derecha = self._insertar(nodo.derecha, fecha, temperatura)
        else:
            nodo.temperatura = temperatura 
            return nodo

        nodo.altura = max(self._altura(nodo.izquierda), self._altura(nodo.derecha)) + 1
        balance = self._balance(nodo)

    
        if balance > 1 and fecha < nodo.izquierda.fecha:
            return self._rotar_derecha(nodo)
        if balance < -1 and fecha > nodo.derecha.fecha:
            return self._rotar_izquierda(nodo)
        if balance > 1 and fecha > nodo.izquierda.fecha:
            nodo.izquierda = self._rotar_izquierda(nodo.izquierda)
            return self._rotar_derecha(nodo)
        if balance < -1 and fecha < nodo.derecha.fecha:
            nodo.derecha = self._rotar_derecha(nodo.derecha)
            return self._rotar_izquierda(nodo)

        return nodo


    def _eliminar(self, nodo, fecha):
        if not nodo:
            return nodo

        if fecha < nodo.fecha:
            nodo.izquierda = self._eliminar(nodo.izquierda, fecha)
        elif fecha > nodo.fecha:
            nodo.derecha = self._eliminar(nodo.derecha, fecha)
        else:
            self._cantidad -= 1
            if not nodo.izquierda:
                return nodo.derecha
            elif not nodo.derecha:
                return nodo.izquierda

            temp = self._min_nodo(nodo.derecha)
            nodo.fecha = temp.fecha
            nodo.temperatura = temp.temperatura
            nodo.derecha = self._eliminar(nodo.derecha, temp.fecha)

        nodo.altura = max(self._altura(nodo.izquierda), self._altura(nodo.derecha)) + 1
        balance = self._balance(nodo)

        if balance > 1 and self._balance(nodo.izquierda) >= 0:
            return self._rotar_derecha(nodo)
        if balance > 1 and self._balance(nodo.izquierda) < 0:
            nodo.izquierda = self._rotar_izquierda(nodo.izquierda)
            return self._rotar_derecha(nodo)
        if balance < -1 and self._balance(nodo.derecha) <= 0:
            return self._rotar_izquierda(nodo)
        if balance < -1 and self._balance(nodo.derecha) > 0:
            nodo.derecha = self._rotar_derecha(nodo.derecha)
            return self._rotar_izquierda(nodo)

        return nodo


    def _buscar(self, nodo, fecha):
        if not nodo:
            return None
        if fecha < nodo.fecha:
            return self._buscar(nodo.izquierda, fecha)
        elif fecha > nodo.fecha:
            return self._buscar(nodo.derecha, fecha)
        else:
            return nodo.temperatura

    def _en_rango(self, nodo, fecha1, fecha2, resultado):
        if not nodo:
            return
        if fecha1 < nodo.fecha:
            self._en_rango(nodo.izquierda, fecha1, fecha2, resultado)
        if fecha1 <= nodo.fecha <= fecha2:
            resultado.append((nodo.fecha, nodo.temperatura))
        if fecha2 > nodo.fecha:
            self._en_rango(nodo.derecha, fecha1, fecha2, resultado)

    def _min_nodo(self, nodo):
        actual = nodo
        while actual.izquierda:
            actual = actual.izquierda
        return actual
    

    def devolver_temperatura(self, fecha_str):
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        temp = self._buscar(self.raiz, fecha)
        if temp is None:                    
            raise ValueError("No se encontró temperatura para esa fecha")
        else:
            return temp

    def guardar_temperatura(self, temperatura, fecha_str):
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        self.raiz = self._insertar(self.raiz, fecha, temperatura)


    def max_temp_rango(self, f1, f2):
        fecha1 = datetime.strptime(f1, "%d/%m/%Y")
        fecha2 = datetime.strptime(f2, "%d/%m/%Y")
        resultado = []
        self._en_rango(self.raiz, fecha1, fecha2, resultado)
        if not resultado:
            raise ValueError("No hay temperaturas en ese rango")
        return max(t for _, t in resultado)

    def min_temp_rango(self, f1, f2):
        fecha1 = datetime.strptime(f1, "%d/%m/%Y")
        fecha2 = datetime.strptime(f2, "%d/%m/%Y")
        resultado = []
        self._en_rango(self.raiz, fecha1, fecha2, resultado)
        if not resultado:
            raise ValueError("No hay temperaturas en ese rango")
        return min(t for _, t in resultado)

    def temp_extremos_rango(self, f1, f2):
        fecha1 = datetime.strptime(f1, "%d/%m/%Y")
        fecha2 = datetime.strptime(f2, "%d/%m/%Y")
        resultado = []
        self._en_rango(self.raiz, fecha1, fecha2, resultado)
        if not resultado:
            raise ValueError("No hay temperaturas en ese rango")
        temperaturas = []
        for fecha, temperatura in resultado:
            temperaturas.append(temperatura)
        return min(temperaturas), max(temperaturas)

    def devolver_temperaturas(self, f1, f2):
        fecha1 = datetime.strptime(f1, "%d/%m/%Y")
        fecha2 = datetime.strptime(f2, "%d/%m/%Y")
        resultado = []
        self._en_rango(self.raiz, fecha1, fecha2, resultado)
        resultado.sort() 
        return [f"{fecha.strftime('%d/%m/%Y')}: {temp} ºC" for fecha, temp in resultado]

    def borrar_temperatura(self, fecha_str):
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        self.raiz = self._eliminar(self.raiz, fecha)

    def cantidad_muestras(self):
        return self._cantidad
    

if __name__ == "__main__":

    lista = Temperaturas_DB()

    lista.guardar_temperatura(25, "01/01/2023")
    lista.guardar_temperatura(30, "15/01/2023")
    lista.guardar_temperatura(22, "28/01/2023")
    lista.guardar_temperatura(35, "01/02/2023")
    lista.guardar_temperatura(20, "10/02/2023")
    lista.guardar_temperatura(27, "15/02/2023")
    lista.guardar_temperatura(32, "01/03/2023")
    lista.guardar_temperatura(24, "10/03/2023")
    lista.guardar_temperatura(29, "20/03/2023")
    lista.guardar_temperatura(26, "31/03/2023")
    
# Función auxiliar para imprimir el contenido de la lista ordenado
    def imprimir_lista_actual(lista):
        temperaturas = lista.devolver_temperaturas("01/01/2023", "31/12/2023")
        print("lista = [")
        for t in temperaturas:
            print(f"  {t}")
        print("]")

    print("\n--- ESTADO INICIAL DE LA LISTA ---")
    imprimir_lista_actual(lista)

    #Probar buscar temperatura
    print("\n--- BUSCAR TEMPERATURA ---")
    fecha = "15/01/2023"
    temp = lista.devolver_temperatura(fecha)
    print(f"Temperatura el {fecha}: {temp} ºC")

    #Probar extremos
    print("\n--- TEMPERATURAS EXTREMAS EN TODO EL RANGO ---")
    extremos = lista.temp_extremos_rango("01/01/2023", "31/12/2023")
    imprimir_lista_actual(lista)
    print(f"temperaturas extremas (min, max): {extremos}")

    #Probar min_temp_rango
    print("\n--- TEMPERATURA MÍNIMA ENTRE 01/02/2023 Y 20/03/2023 ---")
    min_temp = lista.min_temp_rango("01/02/2023", "20/03/2023")
    print(f"temperatura mínima: {min_temp} ºC")

    #Probar max_temp_rango
    print("\n--- TEMPERATURA MÁXIMA ENTRE 01/02/2023 Y 20/03/2023 ---")
    max_temp = lista.max_temp_rango("01/02/2023", "20/03/2023")
    print(f"temperatura máxima: {max_temp} ºC")

    #Probar devolver_temperaturas
    print("\n--- TEMPERATURAS ENTRE 01/02/2023 Y 15/03/2023 ---")
    rango = lista.devolver_temperaturas("01/02/2023", "15/03/2023")
    for r in rango:
        print(r)

    #Probar borrar temperatura
    print("\n--- BORRAR TEMPERATURA DE 10/02/2023 ---")
    lista.borrar_temperatura("10/02/2023")
    imprimir_lista_actual(lista)

    #Verificar que fue eliminada
    print("\n--- BUSCAR TEMPERATURA DE 10/02/2023 (espera error) ---")
    try:
        lista.devolver_temperatura("10/02/2023")
    except ValueError as e:
        print(f"Error: {e}")

    #Probar cantidad de muestras
    print("\n--- CANTIDAD DE MUESTRAS ---")
    print(f"Cantidad total de temperaturas almacenadas: {lista.cantidad_muestras()}")