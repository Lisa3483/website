from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask, render_template, request
import random
import string
from flask_mail import Mail, Message

app = Flask(__name__)


@app.route('/wallet')
def profil():
    param={}
    param['username'] = 'hferrvreverv'
    param['userid'] = '132334234'
    return render_template('wallet1.html', **param)


if __name__ == '__main__':
    app.run(debug=True)
