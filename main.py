from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from data.main import movies

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
    return movies


@app.get('/movies/{id}', tags=['movies'])
def get_movie_by_id(id: int):
    movie = list(filter(lambda movie : movie['id'] == id, movies))
    return movie if len(movie) > 0 else []


@app.get('/movies/', tags=['movies'])
def get_movies_by_category(category: str):
    category = category.strip().lower()
    movies_by_category = list(
        filter(lambda movie: movie['category'].lower() == category, movies)
    )
    return movies_by_category if len(movies_by_category) > 0 else []
