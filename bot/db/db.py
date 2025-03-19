"""
Подключение к PostgreSQL
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from bot.config import DB_URL
from bot.db.models import Base

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Создание таблиц в базе данных"""
    Base.metadata.create_all(bind=engine)