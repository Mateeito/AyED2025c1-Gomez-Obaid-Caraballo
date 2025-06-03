# Archivo de test para realizar pruebas unitarias del modulo1
import unittest
from modules.temperaturas_db import Temperaturas_DB

class TestTemperaturasDB(unittest.TestCase):
    def setUp(self):
        self.db = Temperaturas_DB()
        # Insertamos datos de prueba
        self.db.agregar_temperatura("01/06/2024", 22)
        self.db.agregar_temperatura("02/06/2024", 24)
        self.db.agregar_temperatura("03/06/2024", 18)

    def test_agregar_y_buscar(self):
        self.assertEqual(self.db.devolver_temperatura("01/06/2024"), 22)
        self.assertEqual(self.db.devolver_temperatura("03/06/2024"), 18)
        self.assertEqual(self.db.devolver_temperatura("05/06/2024"), "Fecha no encontrada")

    def test_borrar(self):
        self.db.borrar_temperatura("02/06/2024")
        self.assertEqual(self.db.devolver_temperatura("02/06/2024"), "Fecha no encontrada")
        with self.assertRaises(KeyError):
            self.db.borrar_temperatura("10/10/2020")

    def test_devolver_temperaturas_rango(self):
        temps = self.db.devolver_temperaturas("01/06/2024", "03/06/2024")
        fechas = [t[0] for t in temps]
        self.assertListEqual(fechas, ["01/06/2024", "02/06/2024", "03/06/2024"])

    def test_min_max_temp_rango(self):
        self.assertEqual(self.db.min_temp_rango("01/06/2024", "03/06/2024"), ("03/06/2024", 18))
        self.assertEqual(self.db.max_temp_rango("01/06/2024", "03/06/2024"), ("02/06/2024", 24))

if __name__ == "__main__":
    unittest.main()
