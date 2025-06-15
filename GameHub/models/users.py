from sqlalchemy import Column,String
from app import db  

class Users(db.Model):
    __tablename__ = "users" 
    nickname = Column(String(30), primary_key = True)
    name = Column(String(30), nullable = False)
    password = Column(String(100), nullable = False)
