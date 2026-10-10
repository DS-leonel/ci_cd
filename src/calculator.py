import os

import configcatclient


def toggle_activo(nombre: str, variable_local: str) -> bool:
    """Lee el toggle de ConfigCat. Si no hay llave, usa la variable local."""
    sdk_key = os.getenv("CONFIGCAT_SDK_KEY")
    if sdk_key:
        cliente = configcatclient.get(sdk_key)
        return bool(cliente.get_value(nombre, False))
    return os.getenv(variable_local, "false").lower() == "true"


class Calculator:
    def suma(self, a: int, b: int) -> int:
        return a + b

    def resta(self, a: int, b: int) -> int:
        return a - b

    def multiplicacion(self, a: int, b: int) -> int:
        if not toggle_activo("multiplicacion", "ENABLE_MULTIPLICACION"):
            raise NotImplementedError("Funcionalidad desactivada")
        return a * b