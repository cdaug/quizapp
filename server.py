from itsdangerous import Signer
from flask import Flask, flash, render_template, request, session, redirect, url_for
from flask.ext.login import LoginManager, UserMixin, current_user, login_user, logout_user
import sqlite3

conn = sqlite3.connect('logins.sqlite')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username VARCHAR(75) NOT NULL UNIQUE, password VARCHAR(75) NOT NULL)""")

c.execute("""CREATE TABLE IF NOT EXISTS quizzes (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(25) NOT NULL UNIQUE, description VARCHAR(250), questions INTEGER NOT NULL)""")

username = "Colin"
c.execute('SELECT password FROM users WHERE username=?', (username,))

conn.commit()
conn.close()

DEBUG=True

app = Flask(__name__)

app.config['SECRET_KEY'] = 'SET T0 4NY SECRET KEY L1KE RAND0M H4SH'

login_manager = LoginManager()
login_manager.init_app(app)

Flask.secret_key = "random"

class UserNotFoundError(Exception):
    pass


# Simple user class base on UserMixin
# http://flask-login.readthedocs.org/en/latest/_modules/flask/ext/login.html#UserMixin
class User(UserMixin):
    '''Simple User class'''
    USERS = {
        'admin':'password'
    }

    def __init__(self, id):
        if not id in self.USERS:
            raise UserNotFoundError()
        self.id = id
        self.password = self.USERS[id]

    @classmethod
    def get(self_class, id):
        '''Return user instance of id, return None if not exist'''
        try:
            return self_class(id)
        except UserNotFoundError:
            return None


# Flask-Login use this to reload the user object from the user ID stored in the session
@login_manager.user_loader
def load_user(id):
    return User.get(id)


@app.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin'))
    else:
        return render_template('login.html')


@app.route('/login/check', methods=['post'])
def login_check():
    # validate username and password
    user = User.get(request.form['username'])
    if (user and user.password == request.form['password']):
        login_user(user)
        return redirect(url_for('admin'))
    else:
        flash('Username or password incorrect')

    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route("/")
def index():
    return render_template('index_test.html')

@app.route("/admin")
def admin():
    if current_user.is_authenticated == True:
        return render_template('admin.html')
    else:
        return redirect(url_for('index'))

@app.route("/about")
def about():
    return render_template('about_test.html')

@app.route("/portfolio")
def portfolio():
    return render_template('portfolio_test.html')

@app.route("/readings")
def readings():
    return render_template('readings_test.html')

@app.route("/aenied")
def aenied():
    return render_template('aeniedvirgil_test.html')

@app.route("/night")
def night():
    return render_template('nightwiesel_test.html')

@app.route("/iliad")
def iliad():
    return render_template('iliadhomer_test.html')

@app.route("/odyssey")
def odyssey():
    return render_template('odysseyhomer_test.html')

@app.route("/donquixote")
def donquixote():
    return render_template('quixotecervantes_test.html')

@app.route("/briscola")
def briscola():
    return render_template('game_test.html')

@app.route("/formSave")
def formSave():
    return render_template('formSave.html')

@app.route("/todo")
def todo():
    return render_template('todo_index.html')

@app.route("/ttt")
def tictactoe():
    return render_template('tictactoe.html')


@app.route("/createQuiz")
def createQuiz():
    if current_user.is_authenticated == True:
        return render_template('quizCreation.html')

    else:
        return redirect(url_for('index'))

@app.route("/updateQuiz")
def updateQuiz():
    pass

@app.route("/deleteQuiz")
def deleteQuiz():
    pass

@app.route("/createUser", methods=['get','post'])
def createUser():
    if current_user.is_authenticated == True:
        return render_template('userCreation.html')

        if request.method == 'POST':
            conn = sqlite3.connect('logins.sqlite')
            c = conn.cursor()
            username = request.form['username']
            password = request.form['password']
            userInputs = [username, password]
            c.execute('INSERT INTO users (username, password) VALUES (?,?)', (userInputs,))
            c.execute('SELECT * FROM users WHERE username=?', (username, ))

            conn.commit()
            conn.close()
    else:
        return redirect(url_for('index'))

@app.route("/updateUser")
def updateUser():
    pass

@app.route("/deleteUser")
def deleteUser():
    pass

if __name__ == "__main__":
    app.run(debug=True)
