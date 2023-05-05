from fastapi import FastAPI, Body
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


@app.post('/movies', tags=['movies'])
def create_movie(
        title: str = Body(),
        overview: str = Body(),
        year: int = Body(),
        rating: float = Body(),
        category: str = Body()
    ):
    movie = {
        'id': movies[-1]['id'] + 1,
        'title': title,
        'overview': overview,
        'year': year,
        'rating':rating,
        'category': category
    }
    movies.append(movie)
    return movie


@app.put('/movies/{id}', tags=['movies'])
def update_movie(
        id: int,
        title: str = Body(),
        overview: str = Body(),
        year: int = Body(),
        rating: float = Body(),
        category: str = Body()
    ):
    for movie in movies:
        if movie['id'] == id:
            movie['title'] = title
            movie['overview'] = overview
            movie['year'] = year
            movie['rating'] = rating
            movie['category'] = category

            return movie

    return []


@app.delete('/movies/{id}', tags=['movies'])
def delete_movie(id: int):
    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)
            return movie

    return []
