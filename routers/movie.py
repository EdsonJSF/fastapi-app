from fastapi import APIRouter, Path, Depends, Query
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field

from config.database import Session
from models.movie import Movie as MovieModel
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService

movie_router = APIRouter()


class Movie(BaseModel):
    title: str = Field(max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(ge=1800)
    rating: float = Field(ge=0, le=10)
    category: str = Field(max_length=15)


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

    # Descomprimiendo el diccionario de peliculas.
    new_movie = MovieModel(**movie.dict())

    # Añadir el nuevo registro a la base de datos
    db.add(new_movie)

    # Actualizar y guardar los cambios.
    db.commit()

    return movie.dict()


@movie_router.put('/movies/{id}', tags=['movies'])
def update_movie(id: int, movie: Movie):
    # Iniciamos una sesión
    db = Session()

    # Comprobar si el registro existe
    result = db.query(MovieModel).filter(MovieModel.id == id).first()

    if not result:
        return []

    # Actualiza los campos
    result.title = movie.title
    result.overview = movie.overview
    result.year = movie.year
    result.rating = movie.rating
    result.category = movie.category

    # Guardar los cambios.
    db.commit()

    return jsonable_encoder(movie)


@movie_router.delete('/movies/{id}', tags=['movies'])
def delete_movie(id: int = Path(ge=1)):
    # Iniciamos una sesión
    db = Session()

    # Comprobar si el registro existe
    result = db.query(MovieModel).filter(MovieModel.id == id).first()

    if not result:
        return []

    # Borrar el registro
    db.delete(result)

    # Guardar los cambios.
    db.commit()

    return result
