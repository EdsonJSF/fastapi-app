from fastapi import FastAPI

# Crea la aplicación (una instancia de FastAPI)
app = FastAPI()

# endpoint
@app.get('/')
def message():
    return 'Hola mundo'