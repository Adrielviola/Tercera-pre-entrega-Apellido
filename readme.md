1. Se crearon las siguientes carpetas y archivos en el directorio principal del proyecto:
Tercera_pre_entrega_viola (carpeta principal del proyecto)
aplicacion (carpeta de la aplicación)
migrations (carpeta para las migraciones de la base de datos)
static, donde se encuentran los template de las paginas (carpeta para archivos estáticos)
templates (carpeta para plantillas HTML)
db.sqlite3 (base de datos SQLite)
manage.py (archivo de gestión del proyecto Django)

2. Se crearon los siguientes modelos en el archivo models.py dentro de la carpeta aplicacion:
usuario (modelo para almacenar información de usuarios)
notebook (modelo para almacenar información de notebooks)
desktop (modelo para almacenar información de computadoras de escritorio)
aio (modelo para almacenar información de todo en uno)
celulares (modelo para almacenar información de celulares)

3. Se realizaron migraciones para crear las tablas correspondientes en la base de datos utilizando el siguiente comando:
python manage.py makemigrations
python manage.py migrate

4. Se crearon los archivos admin.py, urls.py y views.py dentro de la carpeta aplicacion para configurar la interfaz de administración, las rutas URL y las vistas de la aplicación.
5. En el archivo admin.py, se registraron los modelos en el panel de administración de Django y se configuraron las opciones de visualización y búsqueda.
6. En el archivo urls.py, se definieron las rutas URL de la aplicación y se asignaron a las vistas correspondientes.
7. En el archivo views.py, se definieron las funciones de vista para cada ruta URL. 
8. Se creó el archivo base.html en la carpeta templates/aplicacion como la plantilla base para todas las páginas HTML. Contiene el encabezado, la barra de navegación y el pie de página comunes.
9. Se crearon las plantillas HTML individuales para cada ruta URL en la carpeta templates/aplicacion. Estas plantillas extienden la plantilla base (base.html) y definen el contenido específico de cada página.
10. Se configuraron los archivos estáticos, como imágenes y archivos CSS, en las plantillas HTML utilizando las etiquetas {% load static %} y {% static %}.
11. Se ejecutó el servidor de desarrollo de Django con el siguiente comando:
python manage.py runserver
Con estos pasos, se configuró un proyecto Django con una aplicación llamada "aplicacion" que contiene modelos para gestionar información de usuarios, notebooks, computadoras de escritorio, todo en uno y celulares.
También se configuraron las vistas y las plantillas HTML correspondientes para cada ruta URL, junto con la configuración de archivos estáticos y el panel de administración de Django.




urls: 172.0.0.1:8000/admin/
http://127.0.0.1:8000/aplicacion/
http://127.0.0.1:8000/aplicacion/formulario/

USUARIO LOCAL(Permisos de vista): usuario_local1234 administrador 
USUARIO LOCAL(Permisos para agregar informacion): belen administrador
USUARIO ADMINISTRADOR: adriel administrador


PD:No se logra finalizar la el formulario para buscar algo en la BD, ya que me arroja un error, el cual no logro encontrarle la solucion. Se adjuntan capturas en la entrega