# notes routers
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models.note import Note
from config.db import client
from schemas.note import note_to_dict, notes_to_dict

note = APIRouter()
templates = Jinja2Templates('templates')


@note.get('/', response_class=HTMLResponse)
def root(request: Request):
    docs = client.notes.notes.find({})
    notes = []
    for doc in docs:
        print(doc)
        notes.append(doc)
    return templates.TemplateResponse('index.html', {'request': request, 'notes': notes})


