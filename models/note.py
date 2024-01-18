from pydantic import BaseModel, Field
from datetime import datetime


class Note(BaseModel):
    title: str = Field(...,max_length=100)
    description: str

class NoteIn(Note):
    pass

class NoteOut(Note):
    id: str
    created: datetime
    updated: datetime