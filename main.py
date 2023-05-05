from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Crea la aplicación (una instancia de FastAPI)
app = FastAPI()

# Documentación del Swagger y de la App
app.title = "FastAPI App"
app.version = "0.0.1"

# Endpoints
@app.get('/', tags=['Home'])
def message():
    return HTMLResponse("""
      <h1>Hola mundo<h1/>
    """)

@app.get('/movies', tags=['movies'])
def get_movies():
    movies = [
        {
            'id': 1,
            'title': 'Avatar',
            'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
            'year': '2009',
            'rating': 7.8,
            'category': 'Acción'
        }
    ]
    return movies
