from modules.nodo_avl import NodoAVL

class ArbolAVL:
    def __init__(self):
        self.raiz = None
        self._cantidad = 0

    def _altura(self, nodo):
        return nodo.altura if nodo else 0

    def _balance(self, nodo):
        return self._altura(nodo.izquierda) - self._altura(nodo.derecha) if nodo else 0

    def _rotar_derecha(self, nodo):
        nodo_iz = nodo.izquierda
        temp = nodo_iz.derecha
        nodo_iz.derecha = nodo
        nodo.izquierda = temp
        nodo.altura = 1 + max(self._altura(nodo.izquierda), self._altura(nodo.derecha))
        nodo_iz.altura = 1 + max(self._altura(nodo_iz.izquierda), self._altura(nodo_iz.derecha))
        return nodo_iz

    def _rotar_izquierda(self, nodo):
        nodo_der = nodo.derecha
        temp = nodo_der.izquierda
        nodo_der.izquierda = nodo
        nodo.derecha = temp
        nodo.altura = 1 + max(self._altura(nodo.izquierda), self._altura(nodo.derecha))
        nodo_der.altura = 1 + max(self._altura(nodo_der.izquierda), self._altura(nodo_der.derecha))
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

        nodo.altura = 1 + max(self._altura(nodo.izquierda), self._altura(nodo.derecha))
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

    def _eliminar(self, nodo, fecha, restar_cantidad=True):
        if not nodo:
            return nodo

        if fecha < nodo.fecha:
            nodo.izquierda = self._eliminar(nodo.izquierda, fecha, restar_cantidad)
        elif fecha > nodo.fecha:
            nodo.derecha = self._eliminar(nodo.derecha, fecha, restar_cantidad)
        else:
            if restar_cantidad:
                self._cantidad -= 1
            if not nodo.izquierda:
                return nodo.derecha
            if not nodo.derecha:
                return nodo.izquierda
            temp = self._min_nodo(nodo.derecha)
            nodo.fecha, nodo.temperatura = temp.fecha, temp.temperatura
            # Aquí le pasamos restar_cantidad=False para no restar cantidad de nuevo
            nodo.derecha = self._eliminar(nodo.derecha, temp.fecha, restar_cantidad=False)

        nodo.altura = 1 + max(self._altura(nodo.izquierda), self._altura(nodo.derecha))
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

    def _min_nodo(self, nodo):
        while nodo.izquierda:
            nodo = nodo.izquierda
        return nodo

    def _en_rango(self, nodo, fecha1, fecha2, resultado):
        if not nodo:
            return
        if fecha1 < nodo.fecha:
            self._en_rango(nodo.izquierda, fecha1, fecha2, resultado)
        if fecha1 <= nodo.fecha <= fecha2:
            resultado.append((nodo.fecha, nodo.temperatura))
        if fecha2 > nodo.fecha:
            self._en_rango(nodo.derecha, fecha1, fecha2, resultado)

    def cantidad(self):
        return self._cantidad

    def insertar(self, fecha, temperatura):
        self.raiz = self._insertar(self.raiz, fecha, temperatura)

    def eliminar(self, fecha):
        self.raiz = self._eliminar(self.raiz, fecha)

    def buscar(self, fecha):
        return self._buscar(self.raiz, fecha)

    def en_rango(self, fecha1, fecha2):
        resultado = []
        self._en_rango(self.raiz, fecha1, fecha2, resultado)
        return resultado