### Proyecto de Reserva de Hoteles

Este proyecto de reserva de hoteles es una aplicación web diseñada para facilitar la gestión de reservas de habitaciones de hotel. A continuación, se detallan los pasos necesarios para configurar y desplegar el proyecto localmente.

#### Configuración del Entorno

1. **Clonar el Repositorio**
   ```
   git clone <URL_del_repositorio>
   cd nombre_del_proyecto
   ```

2. **Crear y Activar Entorno Virtual (env)**

   **Linux**
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

   **Windows**
   ```bash
   python -m venv env
   .\env\Scripts\activate
   ```

3. **Instalar Dependencias**
   ```bash
   pip install -r requirements.txt
   ```

#### Configuración de la Base de Datos

4. **Configurar la Base de Datos**
   - Asegúrate de tener configurada una base de datos compatible (ej. PostgreSQL, MySQL, SQLite).
   - Actualiza la configuración de la base de datos en `settings.py`.

5. **Migraciones de la Base de Datos**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

#### Ejecutar el Servidor de Desarrollo

6. **Iniciar el Servidor de Desarrollo**
   ```bash
   python manage.py runserver
   ```

   El servidor se ejecutará por defecto en `http://127.0.0.1:8000/`.

#### Acceso a la Aplicación

Una vez que el servidor esté en funcionamiento, abre un navegador web y navega a `http://127.0.0.1:8000/` para acceder a la aplicación de reserva de hoteles.

#### Notas Adicionales

- Asegúrate de tener Python y pip instalados en tu sistema.
- Revisa y ajusta la configuración de `settings.py` según sea necesario para tu entorno de desarrollo.
- Para desplegar en un entorno de producción, considera configuraciones adicionales de seguridad y optimización.
