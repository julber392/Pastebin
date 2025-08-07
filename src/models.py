from sqlalchemy import Column, Integer, String
from src.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(String, index=True)
    hashed_data = Column(String, index=True)
