
from sqlalchemy import Column, String, Integer

from config.database import Base


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(length=50))