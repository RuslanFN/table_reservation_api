from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlmodel import Session
from db import get_session
from services import ReservationService
from schemas import CreateReservation

router = APIRouter()

@router.get('/reservations/')
def get_reservation(session: Session = Depends(get_session)):
    service = ReservationService(session)
    return service.get_reservations()

@router.post('/reservations/')
def create_reservation(reservation_data: CreateReservation, session: Session = Depends(get_session)):
    service = ReservationService(session)
    try:
        new_reservation = service.create_reservation(reservation_data)
        return {'status': 200, 'result': new_reservation}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except LookupError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete('/reservations/{id}')
def delete_reservation(id: int, session: Session = Depends(get_session)):
    service = ReservationService(session)
    try:
        result = service.delete_reservation(id)
        return {'status': 200, 'result': result}
    except LookupError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail=f'Невозможно удалить бронь')