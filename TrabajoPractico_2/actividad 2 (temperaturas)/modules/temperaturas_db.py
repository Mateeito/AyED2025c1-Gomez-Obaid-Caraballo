from datetime import datetime
from modules.arbol_avl import ArbolAVL

class Temperaturas_DB:
    def __init__(self):
        self.arbol = ArbolAVL()

    def _convertir_fecha(self, fecha_str):
        return datetime.strptime(fecha_str, "%d/%m/%Y")
    

    def guardar_temperatura(self, temperatura, fecha_str):
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        self.arbol.insertar(fecha, temperatura)

    def devolver_temperatura(self, fecha_str):
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        temp = self.arbol.buscar(fecha)
        if temp is None:
            raise ValueError("No se encontró temperatura para esa fecha")
        return temp

    def borrar_temperatura(self, fecha_str):
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        self.arbol.eliminar(fecha)

    def cantidad_muestras(self):
        return self.arbol.cantidad()

    def max_temp_rango(self, f1, f2):
        r = self.arbol.en_rango(self._convertir_fecha(f1), self._convertir_fecha(f2))
        if not r:
            raise ValueError("No hay temperaturas en ese rango")
        return max(t for _, t in r)

    def min_temp_rango(self, f1, f2):
        r = self.arbol.en_rango(self._convertir_fecha(f1), self._convertir_fecha(f2))
        if not r:
            raise ValueError("No hay temperaturas en ese rango")
        return min(t for _, t in r)

    def temp_extremos_rango(self, f1, f2):
        r = self.arbol.en_rango(self._convertir_fecha(f1), self._convertir_fecha(f2))
        if not r:
            raise ValueError("No hay temperaturas en ese rango")
        ts = [t for _, t in r]
        return min(ts), max(ts)

    def devolver_temperaturas(self, f1, f2):
        r = self.arbol.en_rango(self._convertir_fecha(f1), self._convertir_fecha(f2))
        r.sort()
        return [f"{f.strftime('%d/%m/%Y')}: {t} ºC" for f, t in r]


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