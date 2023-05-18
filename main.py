from fastapi import FastAPI, Path, Depends, Query
from fastapi.responses import HTMLResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field

# App components
from config.database import Base, engine, Session
from models.movie import Movie as MovieModel
from middlewares.error_handler import ErrorHandler
from middlewares.jwt_bearer import JWTBearer

# Helpers
from jwt_manager import create_token

# Crea la aplicación (una instancia de FastAPI)
app = FastAPI()

# Documentación del Swagger y de la App
app.title = "FastAPI App"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)

Base.metadata.create_all(bind=engine)


class Movie(BaseModel):
    # id: Optional[int] = None
    title: str = Field(max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(ge=1800)
    rating: float = Field(ge=0, le=10)
    category: str = Field(max_length=15)


class User(BaseModel):
    email: str
    password: str


# Endpoints
@app.get('/', tags=['Home'])
def message():
    return HTMLResponse("""
      <h1>Hola mundo<h1/>
    """)


@app.post('/auth', tags=['auth'])
def create_user(user: User):
    if user.email == "string" and "string":
        token: str = create_token(user.dict())
    return token


@app.get('/movies', tags=['movies'], dependencies=[Depends(JWTBearer())])
def get_movies():
    # Iniciamos una sesión
    db = Session()

    # Realizamos la consulta
    result = db.query(MovieModel).all()

    # Retornamos la consulta con jsonable_encoder
    return jsonable_encoder(result)


@app.get('/movies/{id}', tags=['movies'])
def get_movie_by_id(id: int = Path(ge=1)):
    # Iniciamos una sesión
    db = Session()

    # Realizamos la consulta para filtrar por id
    result = db.query(MovieModel).filter(MovieModel.id == id).first()

    # Retornamos la consulta con jsonable_encoder
    return jsonable_encoder(result) if result else []


@app.get('/movies/', tags=['movies'])
def get_movies_by_category(category: str = Query(max_length=15)):
    # Iniciamos una sesión
    db = Session()

    # Realizamos la consulta para filtrar por id
    category = category.strip().lower()
    result = db.query(MovieModel).filter(MovieModel.category == category).all()

    # Retornamos la consulta con jsonable_encoder
    return jsonable_encoder(result) if result else []


@app.post('/movies', tags=['movies'])
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


@app.put('/movies/{id}', tags=['movies'])
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

    return jsonable_encoder(result)


@app.delete('/movies/{id}', tags=['movies'])
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
