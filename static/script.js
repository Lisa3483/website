
function spin() {
    var value = document.getElementById("spinButton").getAttribute("data-value");
    var roulette = document.getElementById('roulette');
    var images = ['1.jpg', '2.jpg', '3.jpg','4.jpg']; // Пути к изображениям
    var index = 0;
    var interval = setInterval(function() {
        index++;
        if (index >= images.length) {
            index = 0;
        }
        roulette.innerHTML = '<img src="static/img/ruletka/'+value+'/' + images[index] + '">';
    }, 100); // Время между сменой изображений (в миллисекундах)

    setTimeout(function() {
        clearInterval(interval);
        // Здесь можно добавить логику для выбора случайного элемента, когда рулетка останавливается
        roulette.innerHTML = '<img src="static/img/ruletka/'+value+'/' + images[Math.floor(Math.random() * images.length)] + '">';
    }, 3000); // Время, через которое рулетка останавливается (в миллисекундах)
}
