import pytest

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b


def test_sumar():
    assert sumar(3, 4) == 7

def test_restar():
    assert restar(10, 3) == 7

def test_multiplicar():
    assert multiplicar(4, 2) == 8

def test_dividir():
    assert dividir(10, 2) == 5

def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)

def restar(a, b):
    return a + b   # error intencional