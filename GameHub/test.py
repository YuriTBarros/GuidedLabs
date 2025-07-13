from models import users, games
from config import db 
from flask import Flask, render_template, request,session, flash, redirect, url_for
from config import app, db
from models import games, users
from api import routes



if __name__ == '__main__':
    with app.app_context():
        all_users = db.session.execute(db.select(users.Users.nickname)).scalars()
        user = 'nickname'
        user_password= db.session.execute(db.select(users.Users.password).where(users.Users.nickname == user)).scalar_one()
        print(user_password)
