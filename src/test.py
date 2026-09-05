"""Archivo de pruebas directas como en el video de Emilio Carrión."""

from calculator import sum_numbers


def test_sum():
    """Prueba básica del tutorial: comprueba que 2 + 2 es 4."""
    assert sum_numbers(2, 2) == 4
