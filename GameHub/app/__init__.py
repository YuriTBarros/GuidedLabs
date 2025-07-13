# app/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

db = SQLAlchemy()

def create_app():
    gamehub_root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    app = Flask(__name__,
                template_folder=os.path.join(gamehub_root_path, 'templates'),
                static_folder=os.path.join(gamehub_root_path, 'static'))

    app.config.from_object(Config)

    db.init_app(app)

    from api.routes import bp_main 
    app.register_blueprint(bp_main)

    return app