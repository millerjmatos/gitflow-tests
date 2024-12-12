import pytest
from calculadora import somar, subtrair, multiplicar, dividir


def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0
    assert somar(0, 0) == 0


def test_subtrair():
    assert subtrair(5, 2) == 3
    assert subtrair(1, -1) == 2


def test_multiplicar():
    assert multiplicar(2, 3) == 6
    assert multiplicar(-2, 3) == -6
    assert multiplicar(0, 5) == 0


def test_dividir():
    assert dividir(6, 2) == 3
    with pytest.raises(ValueError):
        dividir(5, 0)
