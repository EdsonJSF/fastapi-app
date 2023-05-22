from models.movie import Movie as MovieModel
from schemas.movie import Movie


class MovieService():
    def __init__(self, db) -> None:
        self.db = db

    def get_movies(self):
        # Realizamos la consulta desde el servicio
        result = self.db.query(MovieModel).all()
        return result

    def get_movie_by_id(self, id):
        # Realizamos la consulta para filtrar por id
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return result

    def get_movies_by_category(self, category):
        category = category.strip().lower()

        # Realizamos la consulta para filtrar por categoria
        result = self.db.query(MovieModel).filter(
            MovieModel.category == category).all()
        return result

    def create_movie(self, movie: Movie):
        # Descomprimiendo el diccionario de peliculas.
        new_movie = MovieModel(**movie.dict())

        # Añadir el nuevo registro a la base de datos
        self.db.add(new_movie)

        # Actualizar y guardar los cambios.
        self.db.commit()

    def update_movie(self, id: int, movie: Movie):
         # Comprobar si el registro existe
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()

        if not result:
            return []

        # Actualiza los campos
        result.title = movie.title
        result.overview = movie.overview
        result.year = movie.year
        result.rating = movie.rating
        result.category = movie.category

        # Guardar los cambios.
        self.db.commit()

    def delete_movie(self, id: int):
        # Comprobar si el registro existe
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()

        if not result:
            return []

        # Borrar el registro
        self.db.delete(result)

        # Guardar los cambios.
        self.db.commit()

        return result
