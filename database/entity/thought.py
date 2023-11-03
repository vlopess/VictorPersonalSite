from database.configs.base import Base
from sqlalchemy import Column, DateTime, Integer, String



class Thought(Base):
    __tablename__ = "Thought"

    id = Column(Integer, primary_key=True)
    descricao = Column(String, nullable=False)
    datapublicacao = Column(DateTime, nullable=False)

    def __init__(self, descricao,datapublicacao):
        self.descricao = descricao
        self.datapublicacao = datapublicacao
    
    def __repr__(self):
        return f"Thought [descricao={self.descricao}, datapublicacao={self.datapublicacao}]"