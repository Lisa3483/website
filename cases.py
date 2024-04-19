import random

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cases_info.db'
db = SQLAlchemy(app)


@app.route('/')
def index():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- Bootstrap CSS -->
    <link rel=stylesheet" href="css/style.css">
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .footer-buttons {
            display: flex;
            justify-content: center;
            margin-top: 700px;
        }

        .case-images {
            display: flex;
            justify-content: center;
            margin-bottom: 60px;
        }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo03" aria-controls="navbarTogglerDemo03" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <a class="navbar-brand" href="#">Navbar</a>

        <div class="collapse navbar-collapse" id="navbarTogglerDemo03">
            <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
                <li class="nav-item active">
                    <a class="nav-link" href="#">Главное меню <span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Кейсы</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Профиль</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Кошелек</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Контакты</a>
                </li>
            </ul>
            <ul class="navbar-nav ml-auto mt-2 mt-lg-000">
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        <img src="pprofil.png">
                    </a>
                    <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                        <a class="dropdown-item" href="#">Регистрация</a>
                        <a class="dropdown-item" href="#">Авторизация</a>
                    </div>
                </li>
            </ul>
        </div>
    </nav>

    <div class="container">
        <form action="/submit" method="post">
            <label>
                Card Number<span class="cdnum">*</span>
                <input type="text" name="cardnumber" placeholder="0000 0000 0000 0000" required>
            </label>
            <label>
                Expiration<span class="exp">*</span>
                <input type="text" name="expiration" placeholder="MM/YY" required>
            </label>
            <label>
                CVV<span class="cvv">*</span>
                <input type="text" name="cvv" placeholder="123" required>
            </label>
            <button type="submit">Submit</button>
        </form>
    </div>

    <div class="case-images">
        <img src="{url_for('static', filename='img/case1.jpg')}" alt="здесь должна была быть картинка, но не нашлась">
        <img src="{url_for('static', filename='img/case2.jpg')}" alt="здесь должна была быть картинка, но не нашлась">
        <img src="{url_for('static', filename='img/case3.jpg')}" alt="здесь должна была быть картинка, но не нашлась">
    </div>

    <div class="footer-buttons">
        <button class="btn btn-primary btn-lg" onclick="window.location.href='/case1'">Открыть кейс 1</button>
        <button class="btn btn-primary btn-lg" onclick="window.location.href='/case2'">Открыть кейс 2</button>
        <button class="btn btn-primary btn-lg" onclick="window.location.href='/case3'">Открыть кейс 3</button>
    </div>

    <!-- Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwjjj1yYfoRSRSRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwwwB6" crossorigin="anonymous"></script>
</body>
</html>'''


@app.route('/case1')
def case1():
    # Ваша логика для кейса 1
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Кейс 1</title>
    <style>
        @import url("https://fonts.googleapis.com/css2?family=Raleway:wght@100&display=swap");
        * {
          box-sizing: border-box;
        }
        body {
          height: 100vh;
          justify-content: center;
          align-items: center;
          font-size: 1.5em;
          font-family: Raleway, Helvetica, sans-serif;
          font-weight: 100;
          background: linear-gradient(to right, #fcf885 0%,#a5c956 46%,#5d8e12 100%);
          margin: 0; 
        }
        .content {
          max-width: 23em;
          border: 1px solid #a8e4a0;
          padding: 0.75em;
          background-color: #EBFEE1;
          filter: drop-shadow(-0.25em 0.25em 0.25em rgba(0, 0, 125, 0.25));
          border-radius: 0.375em;
          position: relative;
        }
        button {
          position: absolute; 
          top: 0; 
          left: 0; 
          margin: 0.5em; 
          font-size: 1em;
          font-family: Raleway, Helvetica, sans-serif;
          background: linear-gradient(to right, #fcf885 0%,#a5c956 46%,#5d8e12 100%);
          border: none;
          color: #fff;
          border-radius: 0.25em;
          padding: 0.5em;
        }
        button:hover,
        button:focus {
          background-color: #eb0062;
        }
    </style>
</head>
<body>
    <div class="content">
        <h1>Кейс 1</h1>
        <p>Это содержимое кейса 1.</p>
        <button onclick="window.location.href='/'">Вернуться на главную</button>
    </div>
</body>
</html>
'''


@app.route('/case2')
def case2():
    # Ваша логика для кейса 2
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel-"stylesheet" herf="css/style.css"
    <title>Кейс 1</title>
</head>
<body>
    <h1>Кейс 1</h1>
    <p>Это содержимое кейса 1.</p>
    <button onclick="window.location.href='/'">Вернуться на главную</button>
</body>
</html>'''


@app.route('/case3')
def case3():
    number = random.randint(1, 5)
    table_name = 'Table_hedgehogs'
    user = SQLAlchemy.session.query(table_name).filter_by(id=number)
    print(user)

    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Кейс 3</title>
    <style>
        /* Стили для позиционирования кнопок */
        .container {
            position: relative;
            width: 100%;
            height: 100%;
        }
        .return-button {
            position: absolute;
            top: 10px;
            left: 10px;
        }
        .open-case-button {
            position: absolute;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            background-color: #4CAF50;
            border: none;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 8px;
        }
        .case-image {
            display: block;
            margin: 0 auto;
            width: 200px; /* Размер изображения кейса */
        }
    </style>
</head>
<body>
    <div class="container">
        <button class="return-button" onclick="window.location.href='/';">Вернуться на главную</button>
        <img class="case-image" src="path/to/your/case/image.jpg" alt="Изображение кейса">
        <button class="open-case-button" onclick="animateCase();">Открыть кейс</button>
    </div>

    <script>
        function animateCase() {
            var images = [
                "path/to/your/animation/image1.jpg",
                "path/to/your/animation/image2.jpg",
                "path/to/your/animation/image3.jpg",
                "path/to/your/animation/image4.jpg"
            ];

            var index = 0;

            var animationInterval = setInterval(function() {
                document.querySelector('.case-image').src = images[index];
                index++;
                if (index === images.length) {
                    clearInterval(animationInterval);
                    // Дополнительные действия после завершения анимации
                }
            }, 1000); // Интервал между сменой изображений (в миллисекундах)
        }
    </script>
</body>
</html>
'''


if __name__ == '__main__':
    app.run(debug=True)
