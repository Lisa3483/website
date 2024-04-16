from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Главная страница</title>
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <!-- Custom CSS -->
    <style>
        .footer-buttons {
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 1000; /* убедитесь, что z-index достаточно большой, чтобы кнопки были поверх другого содержимого */
        }
        
        .footer-buttons button {
            margin-right: 10px; /* Увеличьте или уменьшите это значение в соответствии с вашими потребностями */
        }

                      .case-images {
            position: fixed;
            bottom: 220px; /* 200px от кнопок + 20px для отступа */
            left: 50%;
            transform: translateX(-50%);
            z-index: 999; /* чтобы изображения кейсов были над кнопками */
        }
        
        .case-images img {
            width: 100px; /* Измените размер изображений по вашему усмотрению */
            margin-right: 10px; /* Увеличьте или уменьшите это значение в соответствии с вашими потребностями */
        }

        /* CSS стили для формы */
        body {
            display: flex;
            height: 100vh;
            justify-content: center;
            align-items: center;
            font-size: 1.5em;
            font-family: Raleway, Helvetica, sans-serif;
            font-weight: 100;
            background: linear-gradient(to right, #fcf885 0%,#a5c956 46%,#5d8e12 100%);
        }
        input {
            padding: 0.6em 0.25em 0;
            font-size: 1.5em;
            height: 2.1em;
            margin-bottom: 0.25ememem;
            border: none;
            border-bottom: 1px solid peachpuff;
            font-family: Raleway, Helvetica, sans-serif;
            font-weight: 100;
            border-radius: 0.25em;
        }
        label span {
            font-size: 0.75em;
        }
        form {
            width: 100%;
            max-width: 23em;
            border: 1px solid #a8e4a0;
            padding: 0.75em;
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            align-items: center;
            background-color: #EBFEE1;
            filter: drop-shadow(-0.25em 0.25em 0.25em rgba(0, 0, 125, 0.25));
            border-radius: 0.375em;
        }
        form label {
            position: relative;
        }
        form label > span {
            position: absolute;
            top: 0.25em;
            left: 0.25em;
        }
        .cdnum span {
            color: #555;
            font-size: 0.8em;
        }
        .cvv {
            width: 25%;
        }
        label,
        input {
 {
 {
            width: 100%;
        }
        .exp {
            width: calc(75% - 0.75em);
        }
        button {
            width: 100%;
            height: 2.75em;
            font-size: 1em;
            font-family: Raleway, Helvetica, sans-serif;
            background: linear-gradient(to right, #fcf885 0%,#a5c956 46%,#5d8e12 100%);
            border: none;
            color: #fff;
            border-radius: 0.25em;
            margin: 0.25em 0 0 0;
            padding: 0.5em;
        }
        button:hover,
        button:focus {
            background-color: #eb0062;
        }
        ::placeholder {
            color: #ccc;
            opacity: 1;
        }
        ::-ms-input-placeholder {
            color: #ccc;
        }
        input:focus {
            outline-color: #eb0062;
        }
    </style>
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo03" aria-controls="navbarTogglerDemo03" aria-expanded="falsefalsefalse" aria-label="ToggleToggleToggle navigation">
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
        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" data data data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
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
            Card Card Card Card
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
    <img src="case1.jpg" alt="Case 1">
    <img src="case2.jpg" alt="Case 2">
    <img src="case3.jpg" alt="Case 3">
</div>

<div class="footer-buttons">
    <button class="btn btn-primary btn-lg" onclick="window.location.href='/case1'">Открыть кейс 1</button>
    <button class="btn btn-primary btn-lg" onclick="window.location.href='/case2'">Открыть кейссс 2</button>
    <button class="btn btn-primary btn-lg" onclick="window.location.href='/case3'">Открыть кейс 3</button>
</div>

<!-- Bootstrap JS -->
<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwjjj1yYfoRSRSRSJoZ+n" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwwwB6" crossorigin="anonymous"></script>
</body>
</html>
'''


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
        body {
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .content {
            text-align: center;
        }

        button {
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="content">
        <h1>Кейс 1</h1>
    </div>
    <button onclick="redirectToVideoPage()">Открыть</button>

    <script>
        function redirectToVideoPage() {
            // Здесь указывается адрес страницы с видео
            window.location.href = "video_page.html";
        }
    </script>
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
    # Ваша логика для кейса 3
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Кейс 1</title>
</head>
<body>
    <h1>Кейс 1</h1>
    <p>Это содержимое кейса 1.</p>
    <button onclick="window.location.href='/'">Вернуться на главную</button>
</body>
</html>'''


if __name__ == '__main__':
    app.run(debug=True)
