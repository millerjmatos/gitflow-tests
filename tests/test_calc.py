# tests/test_calculadora.py
import unittest
from src.calculadora import Calculadora


class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_soma(self):
        self.assertEqual(self.calc.soma(2, 3), 5)

    def test_subtracao(self):
        self.assertEqual(self.calc.subtracao(5, 3), 2)


if __name__ == '__main__':
    unittest.main()
