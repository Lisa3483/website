from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask, render_template, request
import random
import string
from flask_mail import Mail, Message

app = Flask(__name__)


@app.route('/profil')
def profil():
    param = {}
    param['username'] = 'hferrvreverv'
    param['userid'] = '132334234'
    return render_template('profil.html', **param)


@app.route('/log_in', methods=['POST'])
def log_in():
    param = {}
    return render_template('log_in.html', **param)


if __name__ == '__main__':
    app.run(debug=True)
