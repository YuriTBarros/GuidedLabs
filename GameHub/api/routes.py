# app/routes.py
from flask import render_template, request, session, flash, redirect, url_for, Blueprint
from sqlalchemy import select, asc
from app import db
from models import games, users

bp_main = Blueprint('main', __name__)

@bp_main.route('/')
def index():
    games_list = db.session.execute(db.select(games.Games).order_by(asc(games.Games.id))).scalars()
    return render_template('list_games.html', title1 = 'Games', games = games_list)

@bp_main.route('/login')
def login():
    next = request.args.get('next')
    return render_template('login.html', next=next )

@bp_main.route('/auth', methods =['POST'])
def auth():
    form_username = request.form['username']
    form_password = request.form['password']
    next_page = request.form['next']
    user_from_db = db.session.execute(select(users.Users).where(users.Users.nickname == form_username)).scalar_one_or_none()
    if user_from_db:
        if form_password == user_from_db.password:
            session['user'] = form_username
            flash(form_username+' logged in successfully.')
            return redirect(next_page)

        else:
            flash('Incorrect password. Please try again.', 'error')
            return redirect(url_for('main.login'))
    else:
        flash('Username not found. Please register or check your username.', 'error')
        return redirect(url_for('main.login')) 

@bp_main.route('/logout')
def logout():
    session['user'] = None
    flash("Logged out.")
    return redirect(url_for('main.index')) 

@bp_main.route('/new')
def new():
    if 'user' not in session or session['user'] == None:
        return redirect(url_for('main.login', next = url_for('main.new'))) 
    games_list = db.session.execute(db.select(games.Games).order_by(asc(games.Games.id))).scalars()
    return render_template('add_game.html', title1 = 'Add Game', games = games_list)

@bp_main.route('/create', methods =['POST',])
def add_game():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']
    game_in_db = db.session.execute(db.select(games.Games).where(games.Games.name == name)).scalar_one_or_none()
    if game_in_db:
        flash("Game already in the database.", 'error')
        return redirect(url_for('main.index')) 
    else:
        game = games.Games(name= name, category = category, console = console)
        db.session.add(game)
        db.session.commit()
        return redirect(url_for('main.index')) 

@bp_main.route('/edit/<int:id>')
def edit_game(id):
    if 'user' not in session or session['user'] == None:
        return redirect(url_for('main.login', next = request.url)) 
    game = db.session.execute(db.select(games.Games).where(games.Games.id == id)).scalar_one_or_none()
    return render_template('edit_game.html', title1 = 'Edit Game', game = game)

@bp_main.route('/update', methods =['POST',])
def update_game():
    pass