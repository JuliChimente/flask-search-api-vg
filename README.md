# Flask Search API

Esta es una aplicación Flask que proporciona un API para buscar en un archivo CSV.

## Requisitos

- Python 3.9 o superior
- Flask 2.3.2
- pytest 7.3.1
- Docker (opcional, para ejecución con contenedor)

## Configuración del entorno

1. Clonar el repositorio:

git clone https://github.com/JuliChimente/flask-search-api-vg.git
cd flask-search-api-vg

2. Crear y activar un entorno virtual:

python -m venv venv
source venv/bin/activate # Mac/Linux
venv/Script/activate # Windows

3. Instalar las dependencias:

pip install -r requirements.txt

## Ejecución de la aplicación

python -m app.main

La aplicación estará disponible en http://localhost:5000/search

## Ejecución de las pruebas unitarias

pytest

Esto ejecutará las pruebas y mostrará el resultado en la consola.
