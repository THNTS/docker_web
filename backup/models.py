import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()


class Messages(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    msg = db.Column(db.String(100))
    val = db.Column(db.Integer)
