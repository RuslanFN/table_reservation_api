from models import Table   
from sqlmodel import Session, select
from schemas import CreateTable, DeleteTable
from typing import List

class TableService:
    
    def __init__(self, session: Session):
        self.session = session
    
    def get_all_tables(self) -> List[Table]:
        return self.session.exec(select(Table)).all()
    
    def create_table(self, data_table: CreateTable) -> Table:
        table = Table(
            name=data_table.name, 
            seats=data_table.seats, 
            location=data_table.location)
        self.session.add(table)
        self.session.commit()
        self.session.refresh(table)
        return table

    def delete_table(self, id: int):
        table = self.session.exec(select(Table).where(Table.id==id)).first()
        if table:
            self.session.delete(table)
            self.session.commit()
            return {'message': f'Стол с id {id} был удалён'}
        raise LookupError(f'Стол с id {id} не существует')

    


