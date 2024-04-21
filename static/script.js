function spin() {
    // Блокируем все кнопки на странице
    var buttons = document.getElementsByTagName("button");
    for (var i = 0; i < buttons.length; i++) {
        buttons[i].disabled = true;
    }

    var value = document.getElementById("spinButton").getAttribute("data-value");
    var roulette = document.getElementById('roulette');
    var images = ['1.jpg', '2.jpg', '3.jpg', '4.jpg'];
    var index = 0;
    var interval = setInterval(function() {
        index++;
        if (index >= images.length) {
            index = 0;
        }
        roulette.innerHTML = '<img src="static/img/ruletka/' + value + '/' + images[index] + '">';
    }, 100); // Время между сменой изображений (в миллисекундах)

    setTimeout(function() {
        clearInterval(interval);
        // Здесь можно добавить логику для выбора случайного элемента, когда рулетка останавливается
        var randomImage = images[Math.floor(Math.random() * images.length)];
        roulette.innerHTML = '<img src="static/img/ruletka/' + value + '/' + randomImage + '">';

        // Проверяем, выиграл ли пользователь

        // Добавляем надпись о выигрыше




        // Ждем 5 секунд перед отправкой AJAX запроса и перенаправлением пользователя
        setTimeout(function() {
            // Отправляем AJAX запрос на сервер
            var xhr = new XMLHttpRequest();
            xhr.open("GET", "/path/to/python/endpoint", true); // Замените "/path/to/python/endpoint" на реальный URL вашего серверного эндпоинта
            xhr.send();

            // Перенаправляем пользователя на главную страницу
            window.location.href = "profil"; // Замените "index.html" на путь к главной странице

            // Разблокируем все кнопки на странице после завершения выполнения кода
            for (var i = 0; i < buttons.length; i++) {
                buttons[i].disabled = false;
            }
        }, 5000);
    }, 3000); // Время, через которое рулетка останавливается (в миллисекундах)
}
