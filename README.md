# 🚀 Proyecto CI/CD con GitHub Actions y Docker

Este proyecto está basado en el tutorial de YouTube **"CI/CD con GitHub Actions en MINUTOS: Automatiza tu Pipeline de Desarrollo"** de **Emilio Carrión (@emcarrio)**.

---

## 🎯 ¿Qué aprenderás y qué contiene este proyecto?

1. **Integración Continua (CI)**:
   - **Calidad de código (Linting)**: Verificación con [Ruff](https://github.com/astral-sh/ruff) (linter ultrarrápido en Rust).
   - **Pruebas automáticas**: Ejecución de suites de pruebas con [Pytest](https://docs.pytest.org/).
2. **Despliegue Continuo (CD)**:
   - **Contenerización**: Creación de una imagen Docker basada en `python:3.11-slim`.
   - **Publicación automática**: Subida de la imagen empaquetada a **GitHub Container Registry (GHCR)** mediante `docker/login-action` y `docker/build-push-action`.

---

## 📁 Estructura del Repositorio

```text
ci_cd/
├── .github/
│   └── workflows/
│       └── test_and_build.yml      # Workflow de GitHub Actions
├── src/
│   ├── calculator.py               # Lógica de la calculadora
│   ├── test_calculator.py          # Suite de pruebas con Pytest
│   ├── test.py                     # Archivo de pruebas simplificado del tutorial
│   └── requirements.txt            # Dependencias fijadas (pytest, ruff)
├── Dockerfile                      # Archivo Docker para empaquetar la app
├── .gitignore                      # Exclusiones de Git
└── README.md                       # Esta guía paso a paso
```

---

## 💻 1. Ejecución y Pruebas en Local

### Instalar dependencias
```bash
pip install -r src/requirements.txt
```

### Ejecutar las pruebas unitarias
```bash
cd src
pytest
```

### Ejecutar el linter de código (Ruff)
```bash
cd src
ruff check .
```

---

## 🧪 2. Pasos para recrear el tutorial del video

El video muestra cómo el CI/CD te protege de errores antes de llegar a producción a través de 3 fases:

### 🔴 Experimento 1: Introducir un Bug en el código
1. Abre [src/calculator.py](file:///src/calculator.py) y cambia temporalmente la función `sum_numbers`:
   ```python
   def sum_numbers(a: float, b: float) -> float:
       return 0  # ❌ Bug intencional
   ```
2. Ejecuta `pytest src/` o sube el commit a GitHub (`git commit -m "add bug"`).
3. **Resultado**: El pipeline fallará en el paso de **Pytest** con `assert 0 == 4`, bloqueando el despliegue de código defectuoso.
4. Corrige el bug volviendo a `return a + b` y vuelve a ejecutar.

---

### 🟡 Experimento 2: Introducir un fallo de Linting (import no utilizado)
1. Abre [src/calculator.py](file:///src/calculator.py) y añade al inicio un import que no se use:
   ```python
   import os  # ❌ Import no utilizado (incumple PEP 8)
   ```
2. Ejecuta `ruff check src/` o sube el commit (`git commit -m "test lint"`).
3. **Resultado**: El pipeline fallará en el paso de **Ruff** indicando `F401: 'os' imported but unused`.
4. Elimina `import os` para que el linter vuelva a estar en verde.

---

### 🟢 Experimento 3: Construcción y Publicación de la imagen Docker en GHCR
1. Cuando todos los tests y linters pasen, GitHub Actions ejecutará automáticamente:
   - `docker/login-action@v3`: Se autentica con `ghcr.io` usando `${{ secrets.GITHUB_TOKEN }}`.
   - `docker/build-push-action@v5`: Construye la imagen con el [Dockerfile](file:///Dockerfile) y la sube al registro de GitHub.
2. **Resultado**: En la página de tu repositorio en GitHub, en el panel lateral derecho verás la sección **Packages** con tu imagen lista para ser descargada con:
   ```bash
   docker pull ghcr.io/<TU_USUARIO>/<TU_REPOSITORIO>:latest
   ```

---

## 🚀 3. Cómo subir este proyecto a tu propio GitHub

1. Inicializa el repositorio Git en la carpeta:
   ```bash
   git init -b main
   ```
2. Añade y haz commit de todos los archivos:
   ```bash
   git add .
   git commit -m "feat: inicializar proyecto CI/CD con GitHub Actions"
   ```
3. Crea un repositorio vacío en tu cuenta de GitHub (por ejemplo, `ci_cd_tutorial`).
4. Conecta tu repositorio local con el remoto y haz push:
   ```bash
   git remote add origin https://github.com/<TU_USUARIO>/<NOMBRE_DEL_REPO>.git
   git push -u origin main
   ```
5. Ve a la pestaña **Actions** en tu repositorio de GitHub para ver tu pipeline ejecutándose en vivo.
