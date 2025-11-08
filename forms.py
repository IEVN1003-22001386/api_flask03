from wtforms import Form, FloatField
from wtforms import StringField, FloatField, EmailField, PasswordField, IntegerField
from wtforms import validators

class UserForm(Form):
    matricula = IntegerField('Matricula', [validators.DataRequired(message="La matricula es obligatoria")])
    nombre=StringField("Nombre", [validators.DataRequired(message="El campo es requerido")])
    apellido=StringField("Apellido", [validators.DataRequired(message="El campo es requerio")])
    correo=EmailField("Correo",[validators.Email(message="Ingrese correo valido")])
    