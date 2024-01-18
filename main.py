# Prateek Thakur 18/01/2024
# imports
from fastapi import FastAPI
import uvicorn
# mongodb connection
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
# env variables
from config import mongo_password
import certifi

app = FastAPI(title='Notes Api', docs_url='/')

uri = f"mongodb+srv://admin:{mongo_password}@notes.oibommt.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri,tlsCAFile=certifi.where())
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, port= 5000)