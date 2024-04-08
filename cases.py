import flask
import sqlite3
import json
import os
app = flask.Flask(__name__)


@app.route("/")
def index():
    return "Привет от приложения Flask"


@app.route('/in')
def index_1():
    return """header, footer {padding: 100px 0}
header {
background: linear-gradient(to right, #c9de96 0%,#8ab66b 44%,#398235 100%);}
header { background: linear-gradient(to right, #fcf885 0%,#a5c956 58%,#a5c956 100%); }
header { background: linear-gradient(to right, #fcf885 0%,#a5c956 46%,#5d8e12 100%);}
h1 {text-align: center}
a.itd_play  {
  display: flex;
  width: 150px;
  height: 50px;
  color: white;
  font-weight: 700;
  text-decoration: none;
  user-select: none;
  padding: .5em 2em;
  outline: none;
  border: 2px solid;
  border-radius: 1px;
  transition: 0.2s;
  justify-content: center;
  align-items: center;
  margin: 30px auto 30px;
}
.rere {
background-color: #398235;
width: 60px;
height: 60px;
border-radius: 50%;
display: flex;
justify-content: center;
align-items: center;
margin: 30px auto;
transition: 0.2s;
}
a.itd_play:hover {background: rgba(255,255,255,.2);}
a.itd_play:active {background: white;}
.rere:hover{background: rgba(255,255,255,.2);}"""


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)