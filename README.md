# Sistema de Seguimiento GPS con Django y React

Este es un proyecto Full-Stack que implementa un sistema de seguimiento de geolocalización en tiempo real. El backend está construido con Django y Django REST Framework, mientras que el frontend es una aplicación de una sola página (SPA) desarrollada con React.

## 🚀 Características Principales

- **Seguimiento en Tiempo Real**: Inicia y detiene el seguimiento de la ubicación GPS del dispositivo.
- **Visualización en Mapa**: Muestra la ubicación actual y la ruta recorrida en tiempo real sobre un mapa interactivo (usando Leaflet).
- **Historial de Sesiones**: Guarda las ubicaciones en una base de datos, agrupadas por sesiones de seguimiento.
- **Visualización de Historial**:
    - Muestra una lista de todas las sesiones guardadas.
    - Permite visualizar la ruta completa de una sesión específica en el mapa.
    - Permite ver la ubicación de un punto individual en el mapa.
- **Gestión de Datos**: Permite eliminar registros de ubicación individuales.
- **API RESTful**: El backend expone endpoints para crear y leer ubicaciones.
- **Preparado para Despliegue**: Configurado con Gunicorn, WhiteNoise y `dj-database-url` para un despliegue sencillo en plataformas como Render o Heroku.

## 🛠️ Tecnologías Utilizadas

### Backend
- **Python 3**
- **Django**
- **Django REST Framework**: Para la creación de la API.
- **PostgreSQL**: Base de datos para producción.
- **SQLite**: Base de datos para desarrollo local.
- **Gunicorn**: Servidor WSGI para producción.
- **WhiteNoise**: Para servir archivos estáticos en producción.

### Frontend
- **React.js**
- **Leaflet**: Para los mapas interactivos.
- **Axios**: Para realizar peticiones a la API del backend.
- **Bootstrap**: Para el diseño y los componentes de la interfaz.
- **UUID**: Para generar identificadores únicos de sesión.

## ⚙️ Instalación y Puesta en Marcha

Sigue estos pasos para configurar el entorno de desarrollo en tu máquina local.

### Prerrequisitos

- **Node.js y npm**: Descargar aquí
- **Python 3 y pip**: Descargar aquí

### 1. Configuración del Backend (Django)

```bash
# 1. Clona el repositorio
git clone <URL-DEL-REPOSITORIO>
cd django-react-geolocation

# 2. Navega a la carpeta del backend
cd backend

# 3. (Recomendado) Crea y activa un entorno virtual
python -m venv venv
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate

# 4. Instala las dependencias de Python
pip install -r requirements.txt

# 5. Aplica las migraciones para crear la base de datos (db.sqlite3)
python manage.py migrate

# 6. Inicia el servidor de Django (se ejecutará en http://127.0.0.1:8000)
python manage.py runserver
```

### 2. Configuración del Frontend (React)

Abre una **nueva terminal** para ejecutar estos comandos.

```bash
# 1. Navega a la carpeta del frontend
cd frontend

# 2. Instala las dependencias de Node.js
npm install

# 3. Inicia la aplicación de React (se abrirá en http://localhost:3000)
npm start
```

¡Listo! Ahora puedes abrir `http://localhost:3000` en tu navegador y comenzar a usar la aplicación. La aplicación de React se comunicará automáticamente con el servidor de Django que se ejecuta en el puerto 8000.

## ☁️ Despliegue

El backend está configurado para ser desplegado en servicios de hosting como Render. Las variables de entorno como `SECRET_KEY` y `DATABASE_URL` serán gestionadas por la plataforma de despliegue. WhiteNoise se encargará de servir los archivos estáticos de Django.