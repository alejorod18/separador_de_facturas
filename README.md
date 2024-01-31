# Separador de Facturas

Este programa permite separar facturas automáticamente.

## Instalación

### Windows

1. **Python 3.10 y pip:**
   - Descarga e instala Python 3.10 desde [python.org](https://www.python.org/downloads/).
   - Asegúrate de marcar la opción "Add Python 3.x to PATH" durante la instalación.

2. **Tesseract:**
   - Descarga e instala Tesseract desde [tesseract-ocr](https://github.com/tesseract-ocr/tesseract).
   - Añade la ruta de instalación de Tesseract al PATH del sistema.

3. **Poppler:**
   - Descarga e instala Poppler desde [poppler](https://poppler.freedesktop.org/).
   - Añade la ruta de instalación de Poppler al PATH del sistema.

4. **Python-Tk:**
   - Python-Tk generalmente viene preinstalado con Python en Windows.

### Linux

1. **Python 3.10 y pip:**
   - Instala Python 3.10 y pip con el gestor de paquetes de tu distribución (por ejemplo, `sudo apt-get install python3.10 python3-pip` para Ubuntu).

2. **Tesseract:**
   - Instala Tesseract con el gestor de paquetes (`sudo apt-get install tesseract-ocr` para Ubuntu).

3. **Poppler:**
   - Instala Poppler con el gestor de paquetes (`sudo apt-get install poppler-utils` para Ubuntu).

4. **Python-Tk:**
   - Instala Python-Tk con el gestor de paquetes (`sudo apt-get install python3-tk` para Ubuntu).

### Mac

1. **Python 3.10 y pip:**
   - Instala Python 3.10 y pip con [Homebrew](https://brew.sh/) (`brew install python@3.10`).

2. **Tesseract:**
   - Instala Tesseract con Homebrew (`brew install tesseract`).

3. **Poppler:**
   - Instala Poppler con Homebrew (`brew install poppler`).

4. **Python-Tk:**
   - Python-Tk generalmente viene preinstalado con Python en macOS.

## Configuración del Entorno

1. Clona este repositorio: `git clone https://github.com/tu-usuario/separador-de-facturas.git`.
2. Entra al directorio: `cd separador-de-facturas`.
3. Crea un entorno virtual (opcional pero recomendado): `python -m venv venv` y actívalo (`source venv/bin/activate` en Linux/Mac o `.\venv\Scripts\activate` en Windows).
4. Instala las dependencias: `pip install -r requirements.txt`.

## Ejecución

1. Asegúrate de que estás en el directorio del proyecto y de que el entorno virtual está activado.
2. Ejecuta el programa: `python separador_de_facturas.py`.
3. Sigue las instrucciones en la consola para separar tus facturas.

¡Listo! Ahora deberías tener el entorno configurado y el programa ejecutándose correctamente.
