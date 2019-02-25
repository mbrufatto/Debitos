from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, HiddenField, SelectField, IntegerField
from wtforms.validators import NumberRange, DataRequired
from wtforms.widgets.html5 import *
from wtforms.fields.html5 import DateField, IntegerField
from .tables import Client, Debit
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app import db

def clients_choise():
    return Client.query.all()

class DebitForm(FlaskForm):
    client_id = QuerySelectField('client_id', 
                        query_factory=clients_choise, get_label='client_name')
    description = TextAreaField('description')
    value = IntegerField(validators=[NumberRange(1000, 9999)])
    date = DateField('date')