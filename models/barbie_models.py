from core.configs import Settings
from sqlalchemy import Column, Integer,String

class BarbieModel(settings.DBBaseModel):
    __tablename__ = 'barbie'
    
    id: int = Column(Integer(),primary_key=True, autoincrement=True)
    nome: str = Column(String(50))
    ano: str = Column (Integer(50))