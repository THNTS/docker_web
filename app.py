from flask import Flask, request, Response
from sqlalchemy import insert

app = Flask(__name__)


@app.route('/submit', methods=["POST"])
def submit():
    ins = users.insert().values(name='jack', fullname='Jack Jones')
    conn = engine.connect()



@app.route('/avg', methods=["GET"])
def avg():
    ...


if __name__ == '__main__':
    app.run("0.0.0.0")
