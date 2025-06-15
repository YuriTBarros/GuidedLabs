from flask import Flask, render_template, request,session, flash, redirect, url_for
from config import app, db

class Game:
    def __init__(self, name, category, console):
        self.name = name
        self.category = category
        self.console = console

game1 = Game('Elden Rings','RPG','PS5')
game2 = Game('Skyrim','RPG','PC')
game3 = Game('God of War','RPG','PS2')
games_list = [game1, game2, game3]


class User:
    def __init__(self, name, nickname, password):
        self.name = name
        self.nickname = nickname
        self.password = password

user1 = User('Dalton','DMan','12345')
user2 = User('Jack','Cake','12345')
user3 = User('Rafaela','Rafa','jaja')

users = {user1.nickname : user1,
         user2.nickname : user2,
         user3.nickname : user3}
        



@app.route('/')
def index():
    return render_template('list_games.html', title1 = 'Games', games = games_list)

@app.route('/login')
def login():
    next = request.args.get('next')
    return render_template('login.html', next=next )

@app.route('/auth', methods =['POST'])
def auth():

    if request.form['username'] in users:
        user = users[request.form['username']]
        if request.form['password'] == user.password:
            session['user'] = request.form['username']
            flash(request.form['username'] +' logged in successfully.')
            next_page = request.form['next']
            return redirect(next_page)
    # if 'password' == request.form['password']:
    #     session['user'] = request.form['username']
    #     flash(request.form['username'] +' logged in successfully.')
    #     next_page = request.form['next']
    #     return redirect(next_page)
    else:
        flash('Try again.')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['user'] = None
    flash("Logged out.")
    return redirect('/')

@app.route('/new')
def new():
    if 'user' not in session or session['user'] == None:
        return redirect(url_for('login', next = url_for('new')))
    return render_template('add_game.html', title1 = 'Add Game', games = games_list)

@app.route('/create', methods =['POST',])
def add_game():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']
    game = Game(name,  category, console)
    games_list.append(game)
    return render_template('list_games.html', title1 = 'Games', games = games_list)