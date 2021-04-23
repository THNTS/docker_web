from flask import Flask, request
from solution.web.models import db
from solution.web import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()
db.init_app(app)
db.create_all()



@app.route('/submit', methods=["POST"])
def submit():
    vars = request.form['data']
    word, new_int = vars.split()

    database.add_instance(Messages, msg=word, val=new_int)
    return json.dumps("Added"), 200


@app.route('/avg', methods=["GET"])
def avg():
    msgs = database.get_all(Messages)
    if cats.length() > 0:
        sum = 0
        for msg in msgs:
            sum += msg.int
        return sum/cats.length(), 200
    else:
        return 0.0, 200


if __name__ == '__main__':
    app.run("0.0.0.0")
