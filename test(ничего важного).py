<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask App</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <style>
        #container {
            text-align: center;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }

        #getDataBtn1 {
            margin-top: 20px; /* Задаем отступ сверху */
        }
    </style>
    <link rel="stylesheet"
          href="https://stackpathstackpathstackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
          integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
          crossorigin="anonymous">
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo03"
            aria-controls="navbarTogglerDemo03" aria-expanded="false" aria-label="Toggle navigation">
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
                <a class="nav-link" href="#">Контонтонтакты</a>
            </li>
        </ul>
        <ul class="navbar-nav ml-auto">
            <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" data-toggle="dropdown"
                   aria-haspopup="true" aria-expanded="false">
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

<div id="container">
    <div id="state1">
        <button id="getDataBtn1">Открой кейс 1</button>
    </div>
    <div id="state2" style="display: none;">
        <button id="getDataBtn2">Открой кейс 2</button>
    </div>
</div>

<button id="changeStateBtn">Сменить состояние первой кнопки</button>

<script>
// Изначальное состояние первой кнопки
var currentState = 1;

$('#getDataBtn1').click(function(){
    if (currentState === 1) {
        // Выполнить действия для первого состояния
        $.ajax({
            url: '/get_data',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ 'case_number': 1 }),
            success: function(response){
                console.log(response);
                alert(response.result);
            },
            error error error: function(error){
                console.log(error);
            }
        });
    }
});

$('#getDataBtn2').click(function(){
    if (currentState === 2) {
        // Выполнить действия для второго состояния
        $.ajax({
            url: '/get_data',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ 'case_number': 2 }),
            success: function(response){
                console.log(response);
                alert(response.result);
            },
            error: function(error){
                console.log(error);
            }
        });
    }
});

$('#getDataBtn3').click(function(){
    if (currentState === 3) {
        // Выполнить действия для третьего состояния
        $.ajax({
            url: '/get_data',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ 'case_number': 3 }),
            success: function(response){
                console.log(response);
                alert(response.result);
            },
            error: function(error){
                console.log(error);
            }
        });
    }
});

// Обработчик для кнопки смены состояния первой кнопки
$('#changeStateBtn').click(function(){
    currentState = (currentState === 1) ? 2 : 1; // Меняем состояние на противоположное
    alert("Состояние первой кнопки изменено на " + currentState);
});

</scriptscriptscript>
</body>
</html>
