#25052022 SE GENERA NUEVO PROYECTO
#…or create a new repository on the command line
#echo "# FORO25MAYO" >> README.md
#git init
#git add README.md
#git commit -m "first commit"
#git branch -M main
#git remote add origin https://github.com/aflores85/FORO25MAYO.git
#git push -u origin main
#…or push an existing repository from the command line
#git remote add origin https://github.com/aflores85/FORO25MAYO.git
#git branch -M main
#git push -u origin main



# fullstack_2022_1c

## Agenda

### Backend
- Python
    - Flask
    - Django Rest Framework  (ORM)

- NodeJS (¿?)

### Frontend

- VueJS
    - Quasar
- React
    - React Boostrap

### DevOps

- Docker
- Docker-Compose
- CI/CD in Gitlab
- Heroku


### Adicionales
- Celery
- Proxy: nginx
- Docker-Swarm
- NoSQL
- gprc


## Calendario
07/03/2022	Introduccion. Preparacion del entorno.
14/03/2022	Flask. API Documentation in code.
21/03/2022	Flask.
28/03/2022	-- Sin clases --
04/04/2022	Flask_restx. Projectizado
11/04/2022	
18/04/2022	
25/04/2022	
02/05/2022	
09/05/2022	
16/05/2022	
23/05/2022	
30/05/2022	
06/06/2022	Entrega TP
13/06/2022	Entrega TP
20/06/2022	-- Feriado --
27/06/2022	RFC


## Aprobacion de la asignatura

### Cursada

- TP: 2 o 3 personas. Tema libre.

### Final

- Entrega (Async). Ampliar el TP en un feature a negociar cuando presentan (Individual).


# Notas de la clase

- Backend (Manejar recursos)
  HTTP (s) 
  SOAP (XML)
  JSON (dict de python)

## REST
- Verbos o métodos:
    - GET: Obtener uno o muchos recursos. 
        * http://www.endpoints.com/users/ --> Listado de todos los usuarios
        * http://www.endpoints.com/users/1/ --> Obtengo el usuario con id 1

    - POST: Crear un nuevo recurso
        * http://www.endpoints.com/users/ --> Crea un recurso, a partir de los datos en el body.

    - PUT: Modificar un recurso entero
        * http://www.endpoints.com/users/2/ --> Modificar un recurso entero, a partir de los datos en el body.

    - PATCH: Modificar una parte de un recurso
        * http://www.endpoints.com/users/2/ --> Modifica un recurso a partir de los datos en el body (campo/s a modificar con valor).

    - DELETE: Eliminar un recurso
        * http://www.endpoints.com/users/2/ --> Eliminar un recurso, pe usuario 2 (No tiene body)

    - OPTIONS: Devuelve que verbos estan disponibles
        * http://www.endpoints.com/users/ --> [GET, POST, ...]


## Herramientas para probar endpoints
1- Postman
2- Insomia
3- curl


Client (request) ---HTTP---> Server


## Endpoints para jugar

* https://httpbin.org

* https://swapi.dev/



## Entornos virtuales en Python

### Instalar paquetes en python
* Mac
```pip3 install <nombre paquete>```

* Linux/Windows
```pip install <nombre paquete>```
```python -m pip install <nombre paquete>```

### Crear el entorno
```virtualenv env ```
o
```python -m virtualenv env ```

### Activar el entorno virtual

* Mac/Linux (WSL)
```source env/bin/activate```

* Windows 
```./env/Scripts/activate```

* Windows (bash)
```source env/Scripts/activate```

### Persistir los paquetes instalados
```pip freeze > requirements.txt```

### Desactivar 
```deactivate```
