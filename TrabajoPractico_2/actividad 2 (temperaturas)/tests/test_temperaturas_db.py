# Archivo de test para realizar pruebas unitarias del modulo1
import unittest
from modules.temperaturas_db import Temperaturas_DB

class TestTemperaturasDB(unittest.TestCase):

    def setUp(self):
        self.db = Temperaturas_DB()
        # Insertamos datos de prueba
        self.db.guardar_temperatura(25.5, "01/01/2023")
        self.db.guardar_temperatura(30.0, "15/01/2023")
        self.db.guardar_temperatura(20.0, "10/01/2023")
        self.db.guardar_temperatura(28.3, "20/01/2023")

    def test_guardar_y_devolver_temperatura(self):
        self.assertEqual(self.db.devolver_temperatura("01/01/2023"), 25.5)
        self.assertEqual(self.db.devolver_temperatura("15/01/2023"), 30.0)
        with self.assertRaises(ValueError):
            self.db.devolver_temperatura("05/01/2023")  # fecha no registrada

    def test_max_temp_rango(self):
        max_temp = self.db.max_temp_rango("01/01/2023", "20/01/2023")
        self.assertEqual(max_temp, 30.0)
        with self.assertRaises(ValueError):
            self.db.max_temp_rango("01/02/2023", "10/02/2023")  # rango sin datos

    def test_min_temp_rango(self):
        min_temp = self.db.min_temp_rango("01/01/2023", "20/01/2023")
        self.assertEqual(min_temp, 20.0)

    def test_temp_extremos_rango(self):
        min_t, max_t = self.db.temp_extremos_rango("01/01/2023", "20/01/2023")
        self.assertEqual(min_t, 20.0)
        self.assertEqual(max_t, 30.0)

    def test_devolver_temperaturas(self):
        listado = self.db.devolver_temperaturas("01/01/2023", "20/01/2023")
        esperado = [
            "01/01/2023: 25.5 ºC",
            "10/01/2023: 20.0 ºC",
            "15/01/2023: 30.0 ºC",
            "20/01/2023: 28.3 ºC",
        ]
        self.assertEqual(listado, esperado)

    def test_borrar_temperatura(self):
        self.db.borrar_temperatura("10/01/2023")
        with self.assertRaises(ValueError):
            self.db.devolver_temperatura("10/01/2023")
        self.assertEqual(self.db.cantidad_muestras(), 3)

    def test_cantidad_muestras(self):
        self.assertEqual(self.db.cantidad_muestras(), 4)
        self.db.borrar_temperatura("01/01/2023")
        self.assertEqual(self.db.cantidad_muestras(), 3)

if __name__ == "__main__":
    unittest.main()
