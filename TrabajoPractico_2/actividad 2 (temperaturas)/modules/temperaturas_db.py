from datetime import datetime
from modules.nodo_avl import NodoAVL



class Temperaturas_DB:
    def __init__(self):
        self.raiz = None    #La raiz del arbol viene a ser basicamente su Nodo principal, es el que se usa de referencia para balancear el arbol
        self._cantidad = 0  #Este numero nos indica la cantidad de temperaturas (con sus fechas) que tenemos cargadas, se inicializa en 0 obviamente, incrementando en 1 a medida que agreguemos nuevas temperaturas
    
    #Las siguientes funciones son funciones internas para balancear correctamente el arbol avl
    
    def _altura(self, nodo):    #Devuelve la altura de un nodo (el que enviemos como argumento de la funcion) del arbol AVL. Esta funcion es importante por que a la hora de insertar un nuevo nodo, o rotar nodos, necesitamos saber los hijos izquierdos y derechos, y no siempre esos hijos existen, asi que si no hacemos la verificacion el programa se puede joder cuando intenta accedes a el atributo ".altura" de un nodo
        if not nodo:        
            return 0            #Si ese nodo no existe, le decimos que devuelva 0
        else:
            return nodo.altura  #Si existe le decimos que si, que devuelva esa altura


    def _balance(self, nodo):   #El balance es la diferencia entre la altura del sub-arbol (conjunto de hijos del nodo) izquierdo y el sub-arbol derecho, y lo necesitamos saber para mantener el arbol bien balanceado
        if not nodo:            #Aca comprobamos lo mismo que en la funcion _altura
            return 0
        else:
            return self._altura(nodo.izquierda) - self._altura(nodo.derecha)    #Aprobechamos la funcion _altura para calcular esto. El balance nos dice lo siguiente: si es positivo, el sub-arbol izquierdo es mas alto, si es negativo, el sub-arbol derecho es mas alto, y si es 0, entonces el arbol esta perfectamente balanceado en dicho nodo
   
    #Miren, sinceramente es un quilombo explicar a detalle como funcionan las rotaciones de balanceo, pero basicamente es guardar hijos en variables temporales (o auxiliares) y luego cambiar posiciones entre ellos. Si tienen dudas busquen un video que lo explique
    def _rotar_derecha(self, nodo):     #En caso de que el nodo este desbalanceado hacia la izquierda, necesita una rotacion hacia la derecha
        x = nodo.izquierda              #En x guardadamos el hijo izquierdo del nodo. Este valor 'x' es quien se va a convertir en la nueva raiz del sub-arbol una vez que sea rotado
        T2 = x.derecha                  #Guardamos el subárbol derecho de x, que va a quedar “colgado” cuando hagamos la rotación

        x.derecha = nodo                #X pasa a ser el nuevo nodo raiz
        nodo.izquierda = T2             #El que antes era el nodo raiz, ahora se convierte en el hijo derecho de x

        nodo.altura = max(self._altura(nodo.izquierda), self._altura(nodo.derecha)) + 1
        x.altura = max(self._altura(x.izquierda), self._altura(x.derecha)) + 1
        return x

    def _rotar_izquierda(self, nodo_a_balancear):   #En caso de que el nodo este desbalanceado hacia la derecha (que el lado derecho sea mas grande), necesita una rotacion hacia la izquierda
        y = nodo_a_balancear.derecha                #Primero, guardamos el valor del nodo que queremos balancerar en una variable llamada "y". Posteriormente vamos a hacer que "y" sea la nueva raiz del sub-arbol una vez que balanceemos todo
        subarbol_auxiliar= y.izquierda              #Le asignamos el valor del hijo izquierdo de y (el nodo que esta desbalanceado)

        y.izquierda = nodo_a_balancear              #Ahora que ya guardamos el valor de y.izquierda en la variable "subarbol_auxiliar" podemos colocar en esa posicion al nodo que queriamos arreglar.
        nodo_a_balancear.derecha = subarbol_auxiliar#Ahora sim el sub-arbol que era inicialmente y.izquierda ahora pasa a ser el nuevo hijo derecho de x

        nodo_a_balancear.altura = max(self._altura(nodo_a_balancear.izquierda), self._altura(nodo_a_balancear.derecha)) + 1
        y.altura = max(self._altura(y.izquierda), self._altura(y.derecha)) + 1
        return y

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

        #Rotaciones necesarias
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

    def guardar_temperatura(self, temperatura, fecha_str):
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        self.raiz = self._insertar(self.raiz, fecha, temperatura)

    def _buscar(self, nodo, fecha):
        if not nodo:
            return None
        if fecha < nodo.fecha:
            return self._buscar(nodo.izquierda, fecha)
        elif fecha > nodo.fecha:
            return self._buscar(nodo.derecha, fecha)
        else:
            return nodo.temperatura

    def devolver_temperatura(self, fecha_str):
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        temp = self._buscar(self.raiz, fecha)
        if temp is None:                    #En caso de que dicha temperatura no exista...
            raise ValueError("No se encontró temperatura para esa fecha")
        return temp

    def _en_rango(self, nodo, fecha1, fecha2, resultado):
        if not nodo:
            return
        if fecha1 < nodo.fecha:
            self._en_rango(nodo.izquierda, fecha1, fecha2, resultado)
        if fecha1 <= nodo.fecha <= fecha2:
            resultado.append((nodo.fecha, nodo.temperatura))
        if fecha2 > nodo.fecha:
            self._en_rango(nodo.derecha, fecha1, fecha2, resultado)

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
        temperaturas = [t for _, t in resultado]
        return min(temperaturas), max(temperaturas)

    def devolver_temperaturas(self, f1, f2):
        fecha1 = datetime.strptime(f1, "%d/%m/%Y")
        fecha2 = datetime.strptime(f2, "%d/%m/%Y")
        resultado = []
        self._en_rango(self.raiz, fecha1, fecha2, resultado)
        resultado.sort() 
        return [f"{fecha.strftime('%d/%m/%Y')}: {temp} ºC" for fecha, temp in resultado]

    def _min_nodo(self, nodo):
        actual = nodo
        while actual.izquierda:
            actual = actual.izquierda
        return actual

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

    def borrar_temperatura(self, fecha_str):
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        self.raiz = self._eliminar(self.raiz, fecha)

    def cantidad_muestras(self):
        return self._cantidad
    

if __name__ == "__main__":

    lista_temperaturas = Temperaturas_DB()
    lista_temperaturas.guardar_temperatura(25.5, "01/01/2024")
    lista_temperaturas.guardar_temperatura(30.1, "02/01/2024")
    lista_temperaturas.guardar_temperatura(22.3, "03/01/2024")

    print(lista_temperaturas.devolver_temperatura("02/01/2024")) 
    print(lista_temperaturas.max_temp_rango("01/01/2024", "03/01/2024"))  
    print(lista_temperaturas.temp_extremos_rango("01/01/2024", "03/01/2024")) 
    print(lista_temperaturas.cantidad_muestras())                           

#Esto deberia volver por consola: 30.1 , 30.1 , (22.3, 30.1) , 3