import unittest   #libreria de pruebas unitarias
from laboratorio_5.gestion_alumnos import buscar_alumno

class TestGestionAlumnos(unittest.TestCase):   #creacion de la lista de la clase

    def setUp(self):   #Creacion de la funcion para la busqueda
        self.alumnos = [
            {"nombre": "Ana", "edad": 20, "carrera": "Ingeniería"},
            {"nombre": "Luis", "edad": 22, "carrera": "Matemáticas"},
            {"nombre": "María", "edad": 21, "carrera": "Física"}
        ]

    def test_buscar_alumno_existente(self):   #funcion de busqueda
        resultado = buscar_alumno(self.alumnos, "Ana")
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado["nombre"], "Ana")

    def test_buscar_alumno_inexistente(self):   #funcion de busqueda en caso de no exixtir
        resultado = buscar_alumno(self.alumnos, "Carlos")
        self.assertIsNone(resultado)

if __name__ == "__main__":  #inicio de la clase
    unittest.main()