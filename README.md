# Servidor de archivos

Bajo la idea de poder crear una herramienta que facilite la carga y descarga de archivos/programas se realiza esta aplicación que utiliza las siguientes herramientas:

* Docker - Para contener la aplicación y uso de distintos servicios sin que estos se vean afectados en el sistema operativo
* Python - Como lenguaje de programación
* Django - Como framework web en su versión 4.2.4
* Django Rest Framework (DRF) - Como modulo de python para convertir la aplicación web en una aplicación que tiene soporte REST
* Celery - Como un servicio de tareas asincronas y planificador de tareas
* Redis - Como servicio distribuido de mensajes, cache y base de datos.
* PostgreSQL - Como manejador de base de datos que utiliza Django para almacenar y hacer uso del framework
* DRF Yest Another Swagger Generator (DRF-yasg) - Como herramienta para documentar los endpoints que escribimos con DRF

# Como Desplegar

