# tests/test_calculadora.py
import unittest
from src.calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()
    
    def test_soma(self):
        self.assertEqual(self.calc.soma(2, 3), 5)
        self.assertEqual(self.calc.soma(-1, 1), 0)
        self.assertEqual(self.calc.soma(0, 0), 0)
    
    def test_subtracao(self):
        self.assertEqual(self.calc.subtracao(5, 3), 2)
        self.assertEqual(self.calc.subtracao(10, 15), -5)
        self.assertEqual(self.calc.subtracao(0, 0), 0)
    
    def test_divisao(self):
        self.assertRaises(ZeroDivisionError, self.calc.divisao, 10, 0)
        self.assertEqual(self.calc.divisao(10, 2), 5)
        self.assertEqual(self.calc.divisao(-6, 2), -3)
