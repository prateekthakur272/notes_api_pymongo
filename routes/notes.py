# notes routers
from fastapi import APIRouter, Body, Depends, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from models.note import NoteIn
from config.db import client
from datetime import datetime
from dataclasses import dataclass
from bson import ObjectId

note = APIRouter()
templates = Jinja2Templates('templates')


@note.get('/', response_class=HTMLResponse)
def root(request: Request):
    docs = client.notes.notes.find({})
    notes = []
    for doc in docs:
        notes.append(doc)
    return templates.TemplateResponse('index.html', {'request': request, 'notes': notes})

@dataclass
class NoteForm:
    title: str = Form()
    description: str = Form()

@note.post('/', response_class=HTMLResponse)
async def add_note(request: Request, form : NoteForm = Depends()):
    note = NoteIn(title=form.title, description=form.description)
    note_data = note.model_dump()
    print(note_data)
    note_data.update({'created':datetime.utcnow(), 'updated':datetime.utcnow()})
    client.notes.notes.insert_one(note_data)
    return root(request)


@note.get('/delete/{id}', response_class=HTMLResponse)
def delete_note(request:Request, id:str):
    client.notes.notes.delete_one({'_id':ObjectId(id)})
    return root(request)

@note.get('/{id}', response_class=HTMLResponse)
def delete_note(request:Request, id:str):
    note = client.notes.notes.find_one({'_id':ObjectId(id)})
    print(note)
    return templates.TemplateResponse('note.html', {'request': request, 'note':note})
