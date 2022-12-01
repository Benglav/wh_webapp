from . import db
from flask_login import UserMixin
from sqlalchemy import func
# from flask_wtf import FlaskForm
# from wtforms import StringField
# from wtforms.validators import DataRequired


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    price = db.Column(db.Float)
    date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(20))
    first_name = db.Column(db.String(15))
    product = db.relationship('Product')

