from flask import Flask, render_template, request
import random
import string
from flask_mail import Mail, Message
from DB.database import UserDatabase

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Укажите SMTP-сервер для отправки писем
app.config['MAIL_PORT'] = 587  # Порт сервера
app.config['MAIL_USE_TLS'] = True  # Использовать TLS
app.config['MAIL_USERNAME'] = 'egorovicegorka87@gmail.com'  # Ваш email для отправки писем
app.config['MAIL_PASSWORD'] = 'kfwz tqrt ejgb kcqq'  # Пароль от вашего email
mail = Mail(app)
db = UserDatabase()


@app.route('/')
def index(flagpass=0):
    param = {}
    param['flagpass'] = flagpass
    return render_template('regestr.html', **param)


def generate_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))


@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    if password != confirm_password:
        return index(flagpass=1)

    verification_code = generate_code()

    msg = Message('Код подтверждения', sender='your-email@example.com', recipients=[email])
    msg.body = f'Ваш код подтверждения: {verification_code}'
    mail.send(msg)
    if db.check_regis(email, username):
        return 'Пользователь уже существует'
    else:
        db.add_user(nickname=username, hashed_password=password, email=email)
        return 'Пользователь успешно зарегестрирован'


@app.route('/login', methods=['POST'])
def log_in():
    email = request.form['email']
    password = request.form['password']
    if db.check_log_in(email, password):
        return 'Вы успешно вошли'
    else:
        return "Данные некоректны"


if __name__ == '__main__':
    app.run(debug=True)
