from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SalonForm(FlaskForm):
    aula = StringField('Aula', validators=[DataRequired()])
    horaEntrada = StringField('Hora de Entrada', validators=[DataRequired()])
    submit = SubmitField("Registrar Salon")
