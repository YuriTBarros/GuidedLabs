from flask import Flask
from flask_sqlalchemy import SQLAlchemy
class Config:
    SECRET_KEY = 'alura'
    SQLALCHEMY_DATABASE_URI = "sqlite:////Users/yuridebarros/Documents/Projects/GuidedLabs/GameHub/database/gamehub.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)