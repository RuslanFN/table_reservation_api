from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime

from typing import Optional

class Reservation(SQLModel, table=True):
    __tablename__ = 'reservations'
    id: int = Field(default=None, primary_key=True)
    customer_name: str = Field(max_length=30)
    reservation_time: datetime
    duration: int = Field(ge=15, le=180)
    table_id: int = Field(foreign_key='tables.id', ondelete='CASCADE', nullable=False)
    table: 'Table' = Relationship(back_populates='reservations')