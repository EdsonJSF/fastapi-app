from fastapi import FastAPI

from config.database import Base, engine
from middlewares.error_handler import ErrorHandler
from routers.home import home_router
from routers.auth import auth_router
from routers.movie import movie_router

# Crea la aplicación (una instancia de FastAPI)
app = FastAPI()

# Documentación del Swagger y de la App
app.title = "FastAPI App"
app.version = "0.0.1"

# Middleware asegura la conección entre la app y los servicios
app.add_middleware(ErrorHandler)

# Endpoints puntos de acceso en una red.
app.include_router(home_router)
app.include_router(auth_router)
app.include_router(movie_router)

Base.metadata.create_all(bind=engine)
