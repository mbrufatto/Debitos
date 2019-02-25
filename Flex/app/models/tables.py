#coding: utf8
from datetime import datetime
from app import db
from babel.numbers import format_currency


def dump_datetime(value):
    if value is None:
        return None
    return [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%S")]

class Client(db.Model):
    __tablename__ = "clients"
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer)
    client_name = db.Column(db.String)

    def __init__(self, client_id, client_name):
        self.client_id = client_id
        self.client_name = client_name

class Debit(db.Model):

    __tablename__ = "debits"
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    description = db.Column(db.Text)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    value = db.Column(db.Float)

    client = db.relationship('Client', foreign_keys=client_id)

    @property
    def serialize(self):
       return {
           'id': self.id,
           'client_id': self.client_id,
           'description': self.description,
           'date': dump_datetime(self.date),
           'value': format_currency(self.value, 'BRL', locale='pt_BR')
       }

    def __init__(self, client_id, description, value, date):
        self.client_id = client_id
        self.description = description
        self.value = value
        self.date = datetime.strptime(date, '%Y-%m-%d')

