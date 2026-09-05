"""Pruebas unitarias para las funciones de la calculadora con pytest."""

import pytest
from calculator import divide_numbers, multiply_numbers, subtract_numbers, sum_numbers


def test_sum_numbers():
    """Verifica que la suma funcione correctamente (ejemplo central del tutorial: 2 + 2 = 4)."""
    assert sum_numbers(2, 2) == 4
    assert sum_numbers(-1, 1) == 0
    assert sum_numbers(0, 0) == 0


def test_subtract_numbers():
    """Verifica la función de resta."""
    assert subtract_numbers(10, 4) == 6
    assert subtract_numbers(0, 5) == -5


def test_multiply_numbers():
    """Verifica la función de multiplicación."""
    assert multiply_numbers(3, 5) == 15
    assert multiply_numbers(-2, 3) == -6


def test_divide_numbers():
    """Verifica la función de división y el manejo de excepciones al dividir por cero."""
    assert divide_numbers(8, 2) == 4
    assert divide_numbers(9, 3) == 3

    with pytest.raises(ValueError, match="No es posible dividir por cero."):
        divide_numbers(10, 0)
