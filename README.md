# FastAPI CRUD - Usuarios

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

Una API REST simple para gestionar usuarios con FastAPI y PostgreSQL. Proporciona operaciones completas de CRUD: crear, leer, actualizar y eliminar usuarios.

## Funcionalidades

- **Operaciones CRUD**: Crear, leer, actualizar y eliminar usuarios.
- **Integración con Base de Datos**: PostgreSQL para persistencia de datos.
- **FastAPI**: Framework de alto rendimiento para construir APIs en Python.
- **Endpoints síncronos y asíncronos**: Compatible con ambos tipos de operaciones.
- **Entrada y salida en JSON**: Facilita la integración con frontends o aplicaciones externas.

## Comenzando

Sigue estas instrucciones para configurar y ejecutar el proyecto localmente.

### Requisitos

- [Python 3.10 o superior](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)

### Installation

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/Troy8203/FastAPI-CRUD---Usuarios.git
   cd base-backend
   ```

2. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

### Iniciar la base de datos(opcional)

1. Start the database container:
   ```bash
   docker-compose up -d
   ```

### Iniciar el servidor

1. Ejecutar el servidor:

   ```bash
   python run.py
   ```

Puedes acceder a la documentación de la API en `http://127.0.0.1:8000/docs`.

## Project Structure

```bash
.
├── 📁 .vscode/               # Configuraciones de vscode
│   └── 📄 settings.json
├── 📁 database/
│   └── 📄 database.sql       # Base de datos
├── 📄 .gitignore             # Gitignore
├── 📄 docker-compose.yml     # Docker compose
├── 📄 main.py                # Aplicación principal
├── 📄 README.md
├── 📄 requirements.txt       # Dependencias
└── 📄 run.py                 # Script para levantar el proyecto
```

## Resultado

Cada endpoint devuelve JSON estructurado y mantiene la consistencia de la base de datos. Al abrir <a href="http://127.0.0.1:8000/docs">http://127.0.0.1:8000/docs<a/> , también puedes probar cada operación desde la interfaz interactiva de FastAPI.

[![image.png](https://i.postimg.cc/HkWHHzDQ/image.png)](https://postimg.cc/vcKCtWmB)
