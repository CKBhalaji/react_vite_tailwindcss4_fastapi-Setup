# backend/models.py (or wherever your declarative base is defined)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# This line is crucial!
Base = declarative_base()

# Your model definitions would follow, inheriting from Base
class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)