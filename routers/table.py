from fastapi import APIRouter, Depends
from fastapi.responses import HTTPException
from db import get_session
from sqlmodel import Session
from sqlalchemy.exc import IntegrityError
from services import TableService
from schemas import CreateTable

router = APIRouter()

@router.get('/tables/')
def get_tables(session: Session = Depends(get_session)):
    service = TableService(session)
    result = service.get_all_tables()
    response = {'status': 200, 'result': result}

@router.post('/tables/')
def create_table(table_data: CreateTable, session: Session = Depends(get_session)):
    service = TableService(session)
    try:
        result = service.create_table(table_data)
        return {'message': 'Стол успешно добавлен', 'data': result}
    except IntegrityError:
        return HTTPException(status_code=409, detail='Невозможно добавить стол с заданными параметрами')
    except Exception:
        raise HTTPException(status_code=400, detail='Стол не добавлен')
    
@router.delete('/tables/{id}')
def delete_table(data_table: DeleteTable, session: Session = Depends(get_session)):
    service = TableService(session)
    try:
        service.delete_table(data_table)
        

    