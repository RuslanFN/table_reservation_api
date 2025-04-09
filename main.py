import uvicorn
from fastapi import FastAPI
from routers import table

app = FastAPI()
app.include_router(table.router)


if __name__ == '__main__':
    uvicorn.run(app=app)