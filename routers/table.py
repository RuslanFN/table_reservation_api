from fastapi import APIRouter, Depends
from db import get_session
from sqlmodel import Session
from services import TableService

router = APIRouter()

@router.get('/tables/')
def get_tables(session: Session = Depends(get_session)):
    service = TableService(session)
    result = service.get_all_tables()
    response = {'status': 200, 'result': result}


    