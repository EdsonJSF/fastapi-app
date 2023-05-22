from fastapi import APIRouter, Path, Depends, Query
from fastapi.encoders import jsonable_encoder

from config.database import Session
from models.movie import Movie as MovieModel
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie

movie_router = APIRouter()


@movie_router.get('/movies', tags=['movies'], dependencies=[Depends(JWTBearer())])
def get_movies():
    # Iniciamos una sesión
    db = Session()

    # Realizamos la consulta desde el servicio
    result = MovieService(db).get_movies()

    # Retornamos la consulta con jsonable_encoder
    return jsonable_encoder(result)


@movie_router.get('/movies/{id}', tags=['movies'])
def get_movie_by_id(id: int = Path(ge=1)):
    # Iniciamos una sesión
    db = Session()

    # Realizamos la consulta para filtrar por id
    result = MovieService(db).get_movie_by_id(id)

    # Retornamos la consulta con jsonable_encoder
    return jsonable_encoder(result) if result else []


@movie_router.get('/movies/', tags=['movies'])
def get_movies_by_category(category: str = Query(max_length=15)):
    # Iniciamos una sesión
    db = Session()

    # Realizamos la consulta para filtrar por categoria
    result = MovieService(db).get_movies_by_category(category)

    # Retornamos la consulta con jsonable_encoder
    return jsonable_encoder(result) if result else []


@movie_router.post('/movies', tags=['movies'])
def create_movie(movie: Movie):
    # Iniciamos una sesión
    db = Session()

    MovieService(db).create_movie(movie)

    return movie.dict()


@movie_router.put('/movies/{id}', tags=['movies'])
def update_movie(id: int, movie: Movie):
    # Iniciamos una sesión
    db = Session()

    MovieService(db).update_movie(id, movie)

    return jsonable_encoder(movie)


@movie_router.delete('/movies/{id}', tags=['movies'])
def delete_movie(id: int = Path(ge=1)):
    # Iniciamos una sesión
    db = Session()

    result = MovieService(db).delete_movie(id)

    return result
