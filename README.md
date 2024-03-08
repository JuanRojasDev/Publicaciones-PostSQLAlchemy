# Postgresql

Instalar postgresql:

https://www.cherryservers.com/blog/how-to-install-and-setup-postgresql-server-on-ubuntu-20-04

Pgadmin web mode: http://127.0.0.1/pgadmin4

# Flask sqlalchemy

https://obikastanya.medium.com/create-completed-restfull-api-with-flask-sql-alchemy-and-jwt-as-authenticator-4edd3f8f26b7

## Activar venv (Linux): 

```json
{".env.publish/bin/activate"}
```

## Activar venv (Windows): 

```json
{".env.publish/Scripts/activate"}
```

## Crear venv si no lo tienes (Windows): 

```json
{"python -m venv .env-publish"}
```

## run (Windows):

```json
{"uvicorn main:app --reload"}
```

# Corrección del error de violación de clave externa

## Descripción del error
El error estaba relacionado con una violación de la clave externa en la base de datos al intentar insertar un valor de client_id en la tabla orders que no existía en la tabla clients.

## Solución
Se corrigió el código para verificar primero si el cliente asociado a la orden existía en la base de datos antes de crear la orden. Esto se logró modificando la lógica de creación de la orden para primero verificar la existencia del cliente y luego crear la orden asociada con ese cliente.

## Cambios realizados
En el endpoint de creación de órdenes (/order/), se agregó una verificación para determinar si el cliente asociado a la orden ya existía en la base de datos antes de crear la orden.
Si el cliente no existía, se creaba uno nuevo; de lo contrario, se utilizaba el cliente existente.
Se corrigieron las referencias a las tablas y columnas en las relaciones entre las clases Order, Client y Item para asegurar la coherencia y evitar posibles errores de referencia.

## Instalar Dependencias:

- python 3.9 +
- sqlalchemy
- Psycopg3-binary
- uvicorn
- fastapi
