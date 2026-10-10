from flask import Flask, jsonify

from calculator import Calculator

app = Flask(__name__)
calc = Calculator()


@app.get("/")
def inicio():
    return jsonify(
        app="Calculadora CI/CD",
        rutas=["/suma/2/3", "/resta/5/3", "/multiplicacion/2/3"],
    )


@app.get("/suma/<int:a>/<int:b>")
def suma(a, b):
    return jsonify(resultado=calc.suma(a, b))


@app.get("/resta/<int:a>/<int:b>")
def resta(a, b):
    return jsonify(resultado=calc.resta(a, b))


@app.get("/multiplicacion/<int:a>/<int:b>")
def multiplicacion(a, b):
    try:
        return jsonify(resultado=calc.multiplicacion(a, b))
    except NotImplementedError:
        return jsonify(error="Funcionalidad desactivada"), 404
