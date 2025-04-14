from sqlmodel import SQLModel

class CreateTable(SQLModel):
    name: str = Field(max_length=15)
    seats: int = Field(ge=1, le=6)
    location: str

class DeleteTable(SQLModel):
    id: int = Field(ge=0)