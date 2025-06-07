from flask import Flask, render_template, request

app = Flask(__name__)

class Game:
    def __init__(self, name, category, console):
        self.name = name
        self.category = category
        self.console = console

game1 = Game('Elden Rings','RPG','PS5')
game2 = Game('Skyrim','RPG','PC')
game3 = Game('God of War','RPG','PS2')
games_list = [game1, game2, game3]

@app.route('/')
def index():
    return render_template('list_games.html', title1 = 'Games', games = games_list)

@app.route('/new')
def new():
    return render_template('add_game.html', title1 = 'Add Game', games = games_list)

@app.route('/create', methods =['POST',])
def add_game():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']
    game = Game(name,  category, console)
    games_list.append(game)
    return render_template('list_games.html', title1 = 'Games', games = games_list)

if __name__ == '__main__':
    app.run(debug = True)