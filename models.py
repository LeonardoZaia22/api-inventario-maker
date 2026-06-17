from sqlalchemy import Column, Integer, String
from database import Base

class Componente(Base):

    __tablename__ = "tb_componentes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    nome = Column(String(100), nullable=False)

    quantidade = Column(Integer, default=0)

    categoria = Column(String(50), nullable=False)

    estado_conservacao = Column(String(50), nullable=False)