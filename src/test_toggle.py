import pytest
from calculator import Calculator


def test_multiplicacion_apagada(monkeypatch):
    monkeypatch.delenv("ENABLE_MULTIPLICACION", raising=False)
    with pytest.raises(NotImplementedError):
        Calculator().multiplicacion(2, 3)


def test_multiplicacion_encendida(monkeypatch):
    monkeypatch.setenv("ENABLE_MULTIPLICACION", "true")
    assert Calculator().multiplicacion(2, 3) == 6