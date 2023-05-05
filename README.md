# FastAPI App

Este es un proyecto para practicar y aprender el framework de desarrollo web FastAPI. Incluye varios ejemplos de cómo utilizar FastAPI para crear y desplegar aplicaciones web.

## Requerimientos

- Python 3.x
- Virtualenv (opcional)

## Instalación

1. Clona este repositorio en tu computadora.
2. Accede al folder del proyecto.
3. Crea y activa un entorno virtual para el proyecto.
4. Instala las dependencias necesarias.
5. Inicia la aplicación

Windows

```sh
py -m venv env
env\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload.
```

Linux Mac

```sh
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload.
```

## Ejemplos de uso

El proyecto incluye varios ejemplos de cómo utilizar FastAPI para crear endpoints, trabajar con bases de datos y autenticación.

```navigator
http://localhost:8000/docs
```

## Contribuciones

¡Las contribuciones son siempre bienvenidas! Si deseas contribuir al proyecto, sigue estos pasos:

- Haz un fork de este repositorio.
- Crea una nueva rama con tu contribución

```git
git checkout -b name_branch
```

- Agrega tus cambios y haz un push a tu rama.

```git
git add .
git commit -m "Funcionalidad"
git push origin name_branch
```

- Haz una pull request para agregar tus cambios al proyecto.
