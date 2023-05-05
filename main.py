from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
# from typing import Optional

from data.main import movies

# Crea la aplicación (una instancia de FastAPI)
app = FastAPI()

# Documentación del Swagger y de la App
app.title = "FastAPI App"
app.version = "0.0.1"

class Movie(BaseModel):
    # id: Optional[int] = None
    title: str
    overview: str
    year: int
    rating: float
    category: str


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


@app.post('/movies', tags=['movies'])
def create_movie(movie: Movie):
    item = {"id":  movies[-1]['id'] + 1}
    item.update(movie.dict())
    movies.append(item)
    return item


@app.put('/movies/{id}', tags=['movies'])
def update_movie(
        id: int,
        movie: Movie
    ):
    for item in movies:
        if item['id'] == id:
            item.update(movie.dict())
            return item

    return []


@app.delete('/movies/{id}', tags=['movies'])
def delete_movie(id: int):
    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)
            return movie

    return []
