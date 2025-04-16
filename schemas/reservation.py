from sqlmodel import SQLModel, Field
from datetime import datetime
class CreateReservation(SQLModel):
    customer_name: str = Field(max_length=30)
    reservation_time: datetime
    duration: int = Field(ge=15, le=180)
    table_id: int