from models import Reservation, Table
from sqlmodel import Session, select
from schemas import CreateReservation
from typing import List
from datetime import timedelta, datetime, timezone

class ReservationService:

    def __init__(self, session: Session):
        self.session = session

    def get_reservations(self) -> List[Reservation]:
        return self.session.exec(select(Reservation)).all()
    
    def create_reservation(self, reservation_data: CreateReservation):
        customer_name = reservation_data.customer_name
        reservation_time = reservation_data.reservation_time.replace(tzinfo=None)
        duration = reservation_data.duration
        table_id = reservation_data.table_id
        table = self.session.exec(select(Table).where(Table.id==table_id)).first()
        exists = False
        if reservation_time <= datetime.utcnow():
            raise ValueError('Время брони должно быть в будущем')
        if not table:
            raise LookupError(f'Не существует стола с id = {table_id}')
        for reservation in table.reservations:
            t_r = reservation.reservation_time
            d = timedelta(minutes=reservation.duration)
            if not (t_r + d < reservation_time) or (reservation_time + timedelta(minutes=duration) < t_r):
                exists = True
                break
        if exists:
            raise ValueError('Данное время занято')
        new_reservation = Reservation(
            customer_name=customer_name,
            reservation_time=reservation_time,
            duration=duration, 
            table_id=table_id)
        self.session.add(new_reservation)
        self.session.commit()
        self.session.refresh(new_reservation)
        return {'status': 200, 'result': new_reservation}
        
    def delete_reservation(self, id: int):
        reservation = self.session.exec(select(Reservation).where(Reservation.id==id)).first()
        if reservation:
            self.session.delete(reservation)
            self.session.commit()
            return {'message': f'Бронь с id {id} была удалёна'}
        raise LookupError(f'Бронь с id {id} не существует')
