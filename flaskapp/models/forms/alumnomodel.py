from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AlumnoForm(FlaskForm):
    id = StringField('ID', validators=[DataRequired()])
    nombre = StringField('Nombre del Alumno', validators=[DataRequired()])
    apellido = StringField("Apellido del Alumno", validators=[DataRequired()])