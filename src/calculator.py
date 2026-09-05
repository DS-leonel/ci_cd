


def sum_numbers(a: float, b: float) -> float:
    """Calcula y retorna la suma de dos números.

    Args:
        a: Primer número.
        b: Segundo número.

    Returns:
        float: Resultado de la suma.
    """
    return a + b


def subtract_numbers(a: float, b: float) -> float:
    """Calcula y retorna la resta de dos números.

    Args:
        a: Primer número.
        b: Segundo número.

    Returns:
        float: Resultado de la resta.
    """
    return a - b


def multiply_numbers(a: float, b: float) -> float:
    """Calcula y retorna la multiplicación de dos números.

    Args:
        a: Primer número.
        b: Segundo número.

    Returns:
        float: Resultado de la multiplicación.
    """
    return a * b


def divide_numbers(a: float, b: float) -> float:
    """Calcula y retorna la división de dos números.

    Args:
        a: Numerador.
        b: Denominador.

    Returns:
        float: Resultado de la división.

    Raises:
        ValueError: Si el denominador es cero.
    """
    if b == 0:
        raise ValueError("No es posible dividir por cero.")
    return a / b


if __name__ == "__main__":
    print(f"2 + 2 = {sum_numbers(2, 2)}")
    print(f"10 - 4 = {subtract_numbers(10, 4)}")
    print(f"3 * 5 = {multiply_numbers(3, 5)}")
    print(f"8 / 2 = {divide_numbers(8, 2)}")
