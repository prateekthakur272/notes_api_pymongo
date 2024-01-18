# Prateek Thakur 18/01/2024
# imports
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
# mongodb connection
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
# env variables
from config import mongo_password
import certifi

app = FastAPI(title='Notes Api')
app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates('templates')

uri = f"mongodb+srv://admin:{mongo_password}@notes.oibommt.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri,tlsCAFile=certifi.where())
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
@app.get('/')
def root(request:Request):
    docs = client.notes.notes.find({})
    notes = []
    for doc in docs:
        print(doc)
        notes.append(doc)
    return templates.TemplateResponse('index.html', {'request':request, 'notes':notes})

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, port= 5000)