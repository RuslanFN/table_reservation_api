import uvicorn
from fastapi import FastAPI
from routers import table, reservation

app = FastAPI()
app.include_router(table.router)
app.include_router(reservation.router)

if __name__ == '__main__':
    uvicorn.run(app=app)