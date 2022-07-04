from flask_login import UserMixin

from database import db


class UserModel(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.Text, nullable=False, unique=True)
    name = db.Column(db.Text)
    password = db.Column(db.Text, nullable=False)
    salt = db.Column(db.LargeBinary)
