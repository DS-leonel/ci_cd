from app import app


def test_suma():
    r = app.test_client().get("/suma/2/3")
    assert r.get_json()["resultado"] == 5


def test_multiplicacion_apagada(monkeypatch):
    monkeypatch.delenv("ENABLE_MULTIPLICACION", raising=False)
    r = app.test_client().get("/multiplicacion/2/3")
    assert r.status_code == 404


def test_multiplicacion_encendida(monkeypatch):
    monkeypatch.setenv("ENABLE_MULTIPLICACION", "true")
    r = app.test_client().get("/multiplicacion/2/3")
    assert r.get_json()["resultado"] == 6
