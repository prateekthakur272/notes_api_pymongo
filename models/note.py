from pydantic import BaseModel, Field
from datetime import datetime


class Note(BaseModel):
    title: str = Field(max_length=100)
    description: str
    last_updated: datetime
