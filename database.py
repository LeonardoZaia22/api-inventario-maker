from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

URL_BANCO_DADOS = "mysql+pymysql://root:@localhost:3306/inova_inventario"

engine = create_engine(URL_BANCO_DADOS)

SessaoLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def obter_banco():
    banco = SessaoLocal()
    try:
        yield banco
    finally:
        banco.close()