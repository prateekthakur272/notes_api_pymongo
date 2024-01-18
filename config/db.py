# mongodb connection

from config.config import mongodb_password
from pymongo import MongoClient
import certifi

uri = f"mongodb+srv://admin:{mongodb_password}@notes.oibommt.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, tlsCAFile=certifi.where())
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


