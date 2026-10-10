import os


class Calculator:
    def suma(self, a: int, b: int) -> int:
        return a + b

    def resta(self, a: int, b: int) -> int:
        return a - b

    def multiplicacion(self, a: int, b: int) -> int:
        if os.getenv("ENABLE_MULTIPLICACION", "false").lower() != "true":
            raise NotImplementedError("Funcionalidad desactivada")
        return a * b