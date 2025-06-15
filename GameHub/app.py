from flask import Flask, render_template, request,session, flash, redirect, url_for
from config import app, db
from models import games, users
from api import routes

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Database created.")
    app.run(debug = True)