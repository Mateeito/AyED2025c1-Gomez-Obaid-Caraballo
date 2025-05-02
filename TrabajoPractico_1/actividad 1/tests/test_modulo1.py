
from modules.ordenamiento_burbuja import ordenamiento_burbuja
from modules.ordenamiento_quicksort import ordenamiento_quicksort
from modules.ordenamiento_por_residuos import ordenamiento_por_residuos
import random           #para que me deje crear numeros aleatorios
import unittest


#hay que comprobar que funcionen correctamente con listas de numeros aleatorios de 5 digitos
#generados aleatoriamente (las listas deben contener como minimo 500 numeros)
 
#primero armamos la lista de numeros aleatorios que podamos usar en todas las pruebas:
def generar_lista_aleatoria(tamaño=500, minimo=10000, maximo=100000):
    lista = random.choices(range(minimo, maximo),k=tamaño)
    return lista
   
class TestFuncionesDeOrdenamiento(unittest.TestCase):

    def setUp(self):                                            # es un metodo especial de unittest que se ejecuta automaticamente antes de cada metodo del test
        self.lista_original = generar_lista_aleatoria()         #creamos la lista aleatoria (desordenada)
        self.lista_esperada = sorted(self.lista_original)       #ordenamos la lista con 'sorted' para saber como seria la misma lista pero ordenada, para posteriormente compararla con el resutado que nos den las funciones de ordenamiento

    def test_ordenamiento_burbuja(self):
        copia_lista_ordenada = self.lista_original.copy()       #crea una copia de la lista original (para no modificarla mientras que trabajamos)
        resultado = ordenamiento_burbuja(copia_lista_ordenada)  #ahora mandamos dicha copia a la funcion, para que asi ordene los numeros
        self.assertEqual(resultado, self.lista_esperada)        #por ultimo verificamos que tanto el ordenamiento llevado a cabo por la funcion como el ordenamiento llevado a cabo por sorted(que sabemos es correcto) sean iguales

    def test_ordenamiento_quicksort(self):
        copia_lista_ordenada = self.lista_original.copy()       
        resultado = ordenamiento_quicksort(copia_lista_ordenada)  
        self.assertEqual(resultado, self.lista_esperada)  

    def test_ordenamiento_radixsort(self):
        copia_lista_ordenada = self.lista_original.copy()       
        resultado = ordenamiento_por_residuos(copia_lista_ordenada)  
        self.assertEqual(resultado, self.lista_esperada)  
        

if __name__ == '__main__':
    unittest.main()