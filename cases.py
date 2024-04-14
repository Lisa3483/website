from flask import Flask, jsonify
import random
import os

app = Flask(__name__)

@app.route('/')
def index():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask App</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
</head>
<body>
    <div id="container" style="text-align:center;">
        <div id="state1">
            <button id="getDataBtn1">Открой кейс 1</button>
        </div>
        <div id="state2" style="display: none;">
            <button id="getDataBtn2">Открой кейс 2</button>
        </div>
    </div>

    <button id="changeStateBtn">Сменить состояние первой кнопки</button>

    <script>
        $(document).ready(function(){
            var currentState = 1; // Изначально сайт находится в первом состоянии
            var currentCase = 1; // Текущий номер кейса

            $('#getDataBtn1').click(function(){
                if (currentState === 1) {
                    // Выполнить действия для первого состояния
                    $.ajax({
                        url: '/get_data',
                        type: 'GET',
                        success: function(response){
                            console.log(response);
                            alert(JSON.stringify(response));
                        },
                        error: function(error){
                            console.log(error);
                        }
                    });
                }
            });

            $('#getDataBtn2').click(function(){
                if (currentState === 2) {
                    // Выполнить действия для второго состояния
                    alert("Another Action performed!");
                }
            });

            // Логика для смены состояния первой кнопки
            $('#changeStateBtn').click(function(){
                if (currentCase <= 3) {
                    $('#getDataBtn1').text('Открой кейс ' + currentCase);
                    currentCase++;
                } else {
                    currentCase = 1;
                }
            });
        });
    </script>
</body>
</html>
'''

@app.route('/get_data', methods=['GET'])
def get_data():
    data = [{'dogs': ('', '', 30)}, {'cats': ('', '', 25)}, {'hedgehogs': (0.05, 10000, 'hedgehog1.png')}]
    data_2 = random.choice(data)
    return jsonify(data_2)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

