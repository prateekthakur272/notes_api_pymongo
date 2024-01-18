# Prateek Thakur 18/01/2024
# imports
from fastapi import FastAPI
import uvicorn

app = FastAPI(title='Notes Api', docs_url='/')

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, port= 5000)