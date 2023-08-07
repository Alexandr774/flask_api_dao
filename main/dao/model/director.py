from marshmallow import Schema, fields

from main.setup_db import db


class Director(db.Model):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()
