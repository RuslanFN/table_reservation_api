from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException, RequestValidationError
from db import get_session
from sqlmodel import Session, Field
from sqlalchemy.exc import IntegrityError
from services import TableService
from schemas import CreateTable, DeleteTable

router = APIRouter()

@router.get('/tables/')
def get_tables(session: Session = Depends(get_session)):
    service = TableService(session)
    result = service.get_all_tables()
    response = {'status': 200, 'result': result}
    return response

@router.post('/tables/')
def create_table(table_data: CreateTable, session: Session = Depends(get_session)):
    service = TableService(session)
    try:
        result = service.create_table(table_data)
        return {'message': 'Стол успешно добавлен', 'data': result}
    
    except IntegrityError as e:
        raise HTTPException(status_code=409, detail=f'Невозможно добавить стол с заданными параметрами.')
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Стол не добавлен., ')
    
@router.delete('/tables/{id}')
def delete_table(id: int, session: Session = Depends(get_session)):
    service = TableService(session)
    try:
        result = service.delete_table(id)
        return {'status': 200, 'result': result}
    except LookupError as e:
        HTTPException(status_code=404, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail=f'Невозможно удалить стол')
        

    