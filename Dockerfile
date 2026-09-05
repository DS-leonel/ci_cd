# Imagen base ligera de Python 3.11
FROM python:3.11-slim

# Directorio de trabajo en el contenedor
WORKDIR /app

# Copiamos el archivo de dependencias e instalamos
COPY src/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código fuente de la aplicación
COPY src/ /app/

# Comando por defecto al ejecutar el contenedor
CMD ["python", "calculator.py"]
