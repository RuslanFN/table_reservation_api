from models import Table   
from sqlmodel import Session, select
from schemas import CreateTable, DeleteTable
from typing import Tuple

class TableService:
    
    def __init__(self, session: Session):
        self.session = session
    
    def get_all_tables(self) -> Tuple[Table]:
        return self.session.exec(select(Table))
    
    def create_table(self, data_table: CreateTable) -> Table:
        table = Table(
            name=data_table.name, 
            seats=data_table.seats, 
            location=data_table.location)
        self.session.add(table)
        self.session.commit()
        self.session.refresh(table)
        return table

    def delete_table(self, table_data: DeleteTable):
        id = table_data.id
        table = self.session.query(Table).filter(Table.id==id).first()
        if table:
            self.session.delete(table)
            self.session.commit()
            return {'message': f'Стол с id {id} был удалён'}
        raise ValueError(message=f'Стол с id {id} не существует')

    


