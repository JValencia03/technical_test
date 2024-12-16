# Technical Test

Prueba técnica

## Requisitos

- Docker

## Instalación

1. Clona el repositorio en tu ordenador.

2. En la raíz del proyecto, crea un archivo llamado .env, en el que incluirás las siguientes variables de entorno:

```env
FLASK_ENV=development
DATABASE_URI=mysql+mysqldb://root:1234@db:3306/technicalTest
```

## Contenedores

1. Construye los contenedores gracias al archivo docker-compose.yml:

```sh
docker-compose up --build
```

2. La aplicación se encuentra en el puerto 5000