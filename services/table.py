from models import Table   
from sqlmodel import Session, select

class TableService:
    
    def __init__(self, session: Session):
        self.session = session
    
    def get_all_tables(self):
        return self.session.exec(select(Table))
        
