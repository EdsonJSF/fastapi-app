from fastapi import FastAPI

# Crea la aplicación (una instancia de FastAPI)
app = FastAPI()

# Documentación del Swagger y de la App
app.title = "FastAPI App"
app.version = "0.0.1"

# endpoint
@app.get('/', tags=['Home'])
def message():
    return 'Hola mundo'