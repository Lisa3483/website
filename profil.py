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
    user_foto = "user_foto.jpg"
    return render_template('profil.html', user_foto=user_foto)


if __name__ == '__main__':
    app.run(debug=True)
