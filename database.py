from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Caminho absoluto ou relativo para o arquivo SQLite
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_URL = "sqlite:///C:/Users/User/Python_Projects/Projeto_SQLite/test(1).db"  # ajustado conforme a estrutura de pastas

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    # Não recria tabelas pois você já tem o schema criado
    pass
