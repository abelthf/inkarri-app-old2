
https://github.com/abelthf/inkarri-app

$ git clone  https://github.com/abelthf/inkarri-app
$ cd inkarri-app
$  docker-compose  -f docker-compose-dev.yml up -d --build

docker-compose -f docker-compose-dev.yml run users python manage.py recreate_db

para ingresar a la base de datos:

$ docker-compose -f docker-compose-dev.yml exec users-db psql -U postgres
CONFIGURACION DE PRUEBAS

CREAR el directorio “tests” en el directorio “project” y dentro  crear los archivos:
1. __init__.py
2. base.py
3. test_config.py
4. test_users.py
