from sqlalchemy import Column, String, Integer
from app import db

class Games(db.Model):
    __tablename__ = "games" 
    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String(100), nullable = False)
    category = Column(String(30), nullable = False)
    console = Column(String(30), nullable = False)