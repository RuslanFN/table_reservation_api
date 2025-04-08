from enum import Enum
from sqlmodel import SQLModel, Field, Relationship
from typing import List
from .reservation import Reservation

class Table(SQLModel):
    __tablename__ = 'tables'
    id: int = Field(default=None, primary_key=True)
    name: str = Field(max_length=15)
    seats: int = Field(le=6)
    location: str
    reservations: List['Reservation'] = Relationship(back_populates='tables')
