from marshmallow import Schema, fields

from main.setup_db import db


class Genre(db.Model):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()
