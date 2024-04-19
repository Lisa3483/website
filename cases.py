import random
from cases_mech import Cases_mechanic
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cases_info.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
@app.route('/')
def index():
    return render_template('style.html')


@app.route('/case1')
def case1():
    number = random.randint(1, 5)
    table_name = 'Table_dogs'
    #user = SQLAlchemy.query(table_name).filter_by(id=number)
    cass = Cases_mechanic()
    #cass.get_win('Table_dogs')
    return render_template('case1.html')


@app.route('/case2')
def case2():
    number = random.randint(1, 5)
    table_name = 'Table_hedgehogs'
    #user = SQLAlchemy.session.query(table_name).filter_by(id=number)
    cass = Cases_mechanic()
    #cass.get_win('Table_hedgehogs')
    return render_template('case2.html')


@app.route('/case3')
def case3():
    number = random.randint(1, 5)
    table_name = 'Table_cats'
    #user = SQLAlchemy.session.query(table_name).filter_by(id=number)
    cass = Cases_mechanic()
    #cass.get_win('Table_cats')

    return render_template('case3.html')


if __name__ == '__main__':
    app.run(debug=True)
