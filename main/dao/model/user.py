from marshmallow import Schema, fields
from main.setup_db import db


class User(db.Model):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    role = db.Column(db.String)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    favorite_genre = db.Column(db.Integer)


class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    password = fields.Str()
    role = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    favorite_genre = fields.Int()
