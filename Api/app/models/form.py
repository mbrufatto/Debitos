from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, HiddenField, SelectField, IntegerField
from wtforms.validators import NumberRange, DataRequired
from wtforms.widgets.html5 import *
from wtforms.fields.html5 import DateField, IntegerField


class DebitForm(FlaskForm):
    clients = SelectField(choices=[("1-Gustavo", 'Gustavo'), ("2-Eduardo", 'Eduardo')])
    description = TextAreaField('description')
    value = IntegerField(validators=[NumberRange(1000, 9999)])
    date = DateField('date')