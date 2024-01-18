# Prateek Thakur 18/01/2024

# imports
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
from routes.notes import note


app = FastAPI(title='Notes Api')
app.mount('/static', StaticFiles(directory='static'), name='static')
app.include_router(note)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, port=5000)
