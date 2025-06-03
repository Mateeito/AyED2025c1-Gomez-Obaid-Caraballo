from datetime import datetime

class Nodo:
    def __init__(self, fecha, temperatura):
        self.fecha = datetime.strptime(fecha, "%d/%m/%Y")
        self.temperatura = temperatura
        self.izquierda = None
        self.derecha = None
        self.altura = 1

class Temperaturas_DB:
    def __init__(self):
        self.raiz = None


    def _parsear_fecha(self, fecha_str):
        """Convierte un string en formato dd/mm/yyyy a un objeto datetime."""
        try:
            return datetime.strptime(fecha_str, "%d/%m/%Y")
        except ValueError:
            raise ValueError(f"Fecha inválida: {fecha_str}. Usar formato dd/mm/yyyy.")

    def _altura(self, nodo):
        return nodo.altura if nodo else 0

    def _balance(self, nodo):
        return self._altura(nodo.izquierda) - self._altura(nodo.derecha) if nodo else 0

    def _actualizar_altura(self, nodo):
        nodo.altura = max(self._altura(nodo.izquierda), self._altura(nodo.derecha)) + 1

    def _rotar_derecha(self, nodo):
        """Rotación simple derecha."""
        nueva_raiz = nodo.izquierda
        nodo.izquierda = nueva_raiz.derecha
        nueva_raiz.derecha = nodo
        self._actualizar_altura(nodo)
        self._actualizar_altura(nueva_raiz)
        return nueva_raiz

    def _rotar_izquierda(self, nodo):
        """Rotación simple izquierda."""
        nueva_raiz = nodo.derecha
        nodo.derecha = nueva_raiz.izquierda
        nueva_raiz.izquierda = nodo
        self._actualizar_altura(nodo)
        self._actualizar_altura(nueva_raiz)
        return nueva_raiz

    def _balancear(self, nodo):
        """Realiza las rotaciones necesarias para balancear el árbol."""
        self._actualizar_altura(nodo)
        balance = self._balance(nodo)

        if balance > 1:
            if self._balance(nodo.izquierda) < 0:
                nodo.izquierda = self._rotar_izquierda(nodo.izquierda)
            return self._rotar_derecha(nodo)
        elif balance < -1:
            if self._balance(nodo.derecha) > 0:
                nodo.derecha = self._rotar_derecha(nodo.derecha)
            return self._rotar_izquierda(nodo)

        return nodo


    def _insertar(self, nodo, fecha, temperatura):
        fecha_dt = self._parsear_fecha(fecha)

        if not nodo:
            return Nodo(fecha, temperatura)

        if fecha_dt < nodo.fecha:
            nodo.izquierda = self._insertar(nodo.izquierda, fecha, temperatura)
        elif fecha_dt > nodo.fecha:
            nodo.derecha = self._insertar(nodo.derecha, fecha, temperatura)
        else:
            nodo.temperatura = temperatura
            return nodo

        return self._balancear(nodo)

    def agregar_temperatura(self, fecha, temperatura):
        """Agrega o actualiza la temperatura de una fecha."""
        self.raiz = self._insertar(self.raiz, fecha, temperatura)

    def _min_valor_nodo(self, nodo):
        actual = nodo
        while actual.izquierda:
            actual = actual.izquierda
        return actual

    def _eliminar(self, nodo, fecha):
        fecha_dt = self._parsear_fecha(fecha)

        if not nodo:
            raise KeyError(f"No existe una entrada para la fecha: {fecha}")

        if fecha_dt < nodo.fecha:
            nodo.izquierda = self._eliminar(nodo.izquierda, fecha)
        elif fecha_dt > nodo.fecha:
            nodo.derecha = self._eliminar(nodo.derecha, fecha)
        else:
            if not nodo.izquierda:
                return nodo.derecha
            elif not nodo.derecha:
                return nodo.izquierda

            temp = self._min_valor_nodo(nodo.derecha)
            nodo.fecha = temp.fecha
            nodo.temperatura = temp.temperatura
            nodo.derecha = self._eliminar(nodo.derecha, temp.fecha.strftime("%d/%m/%Y"))

        return self._balancear(nodo)

    def borrar_temperatura(self, fecha):
        """Elimina la temperatura asociada a una fecha."""
        self.raiz = self._eliminar(self.raiz, fecha)

    def _buscar(self, nodo, fecha):
        fecha_dt = self._parsear_fecha(fecha)
        if not nodo:
            return None
        if fecha_dt < nodo.fecha:
            return self._buscar(nodo.izquierda, fecha)
        elif fecha_dt > nodo.fecha:
            return self._buscar(nodo.derecha, fecha)
        else:
            return nodo.temperatura

    def devolver_temperatura(self, fecha):
        """Devuelve la temperatura registrada en una fecha específica."""
        temp = self._buscar(self.raiz, fecha)
        return temp if temp is not None else "Fecha no encontrada"

    def _en_rango(self, nodo, fecha1, fecha2, resultado):
        if not nodo:
            return
        if fecha1 < nodo.fecha:
            self._en_rango(nodo.izquierda, fecha1, fecha2, resultado)
        if fecha1 <= nodo.fecha <= fecha2:
            resultado.append((nodo.fecha.strftime("%d/%m/%Y"), nodo.temperatura))
        if nodo.fecha < fecha2:
            self._en_rango(nodo.derecha, fecha1, fecha2, resultado)

    def devolver_temperaturas(self, f1, f2):
        """Devuelve todas las temperaturas entre dos fechas."""
        fecha1 = self._parsear_fecha(f1)
        fecha2 = self._parsear_fecha(f2)
        resultado = []
        self._en_rango(self.raiz, fecha1, fecha2, resultado)
        return resultado

    def min_temp_rango(self, f1, f2):
        """Devuelve la temperatura mínima entre dos fechas."""
        temps = self.devolver_temperaturas(f1, f2)
        return min(temps, key=lambda x: x[1]) if temps else None

    def max_temp_rango(self, f1, f2):
        """Devuelve la temperatura máxima entre dos fechas."""
        temps = self.devolver_temperaturas(f1, f2)
        return max(temps, key=lambda x: x[1]) if temps else None

if __name__ == "__main__":
    db = Temperaturas_DB()
    db.agregar_temperatura("01/06/2024", 22)
    db.agregar_temperatura("02/06/2024", 24)
    db.agregar_temperatura("03/06/2024", 18)
    db.agregar_temperatura("04/06/2024", 20)
    db.agregar_temperatura("05/06/2024", 26)
    db.agregar_temperatura("06/06/2024", 19)
    db.agregar_temperatura("07/06/2024", 21)
    db.agregar_temperatura("08/06/2024", 25)

    print("--- TEMPERATURA DEL 03/06/2024 ---")
    print(db.devolver_temperatura("03/06/2024"))

    print("\n--- RANGO 03/06 al 06/06 ---")
    print(db.devolver_temperaturas("03/06/2024", "06/06/2024"))

    print("\n--- MÍNIMA EN RANGO ---")
    print(db.min_temp_rango("03/06/2024", "06/06/2024"))

    print("\n--- MÁXIMA EN RANGO ---")
    print(db.max_temp_rango("03/06/2024", "06/06/2024"))

    print("\n--- BORRANDO 04/06/2024 ---")
    db.borrar_temperatura("04/06/2024")
    print(db.devolver_temperatura("04/06/2024"))

    print("\n--- BORRANDO FECHA INEXISTENTE (05/05/2022) ---")
    try:
        db.borrar_temperatura("05/05/2022")
    except KeyError as e:
        print(f"Error: {e}")
