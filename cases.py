import flask
import sqlite3
import json
import os
app = flask.Flask(__name__)


@app.route('/')
def index_1():
    return """<iframe width="1140" height="641" src="https://www.youtube.com/embed/evQD6oZe8oQ" title="Бобр.mp4" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>"""


@app.route('/index')
def index_2():
    conn = sqlite3.connect('cases_info.db')
    cursor = conn.cursor()
    if case_name in cases_name:
        pass
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Проигрывание видео</title>
    <style>
        body, html {
            margin: 0;
            padding: 0;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #f0f0f0;
        }
        .video-container {
            max-width: 800px;
            max-height: 600px;
            overflow: hidden;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.3);
        }
        video {
            width: 100%;
            height: 100%;
        }
    </style>
</head>
<body>
    <div class="video-container">
        <video controls>
            <source src="sample-5s.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>
</body>
</html>
'''



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)