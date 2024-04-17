from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask, render_template, request
import random
import string
from flask_mail import Mail, Message
from DB.database import UserDatabase


app = Flask(__name__, template_folder='static/templates')

db = UserDatabase()
NAME = ''
ID = ''
FLAG_IN = 0


@app.route('/')
def index():
    global FLAG_IN
    param = {}
    param['flagau'] = FLAG_IN
    print(FLAG_IN, NAME, ID)

    return render_template('main_menu.html', **param)


@app.route('/profil')
def profil():
    param = {}
    param['username'] = NAME
    param['userid'] = ID
    return render_template('profil.html', **param)


@app.route('/log_in', methods=['GET'])
def log_in():
    param = {}
    return render_template('log_in.html', **param)


@app.route('/registr', methods=['GET'])
def regist(flagpass=0):
    param = {}
    param['flagpass'] = flagpass
    return render_template('regestr.html', **param)


@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    if password != confirm_password:
        return regist(flagpass=1)

    if db.check_regis(email, username):
        return regist(flagpass=2)
    else:
        db.add_user(nickname=username, hashed_password=password, email=email)
        return 'Пользователь успешно зарегестрирован'


'''@app.route('/log', methods=['POST'])
def logs():
    global NAME
    global ID
    global FLAG_IN
    email = request.form['email']
    password = request.form['password']
    if db.check_log_in(email, password):
        name, id_ = db.check_log_in(email, password)
        NAME = name@app.route('/register', methods=['POST'])'''
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    if password != confirm_password:
        return regist(flagpass=1)

    if db.check_regis(email, username):
        return regist(flagpass=2)
    else:
        db.add_user(nickname=username, hashed_password=password, email=email)
        return 'Пользователь успешно зарегестрирован'


@app.route('/log', methods=['POST'])
def log():
    global NAME
    global ID
    global FLAG_IN
    email = request.form['email']
    password = request.form['password']
    if db.check_log_in(email, password):
        name, id_ = db.check_log_in(email, password)
        NAME = name
        ID = id_
        FLAG_IN = 1
        print(FLAG_IN)
        return profil()

@app.route('/wallet', methods=['GET'])
def wallet():
    param = {}
    return render_template('wallet.html', **param)


if __name__ == '__main__':
    app.run(debug=True)