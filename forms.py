from wtforms import Form, FloatField
from wtforms import StringField, FloatField, EmailField, PasswordField, IntegerField
from wtforms import validators
from wtforms import RadioField, SelectMultipleField


class UserForm(Form):
    matricula = IntegerField('Matricula', [validators.DataRequired(message="La matricula es obligatoria")])
    nombre=StringField("Nombre", [validators.DataRequired(message="El campo es requerido")])
    apellido=StringField("Apellido", [validators.DataRequired(message="El campo es requerio")])
    correo=EmailField("Correo",[validators.Email(message="Ingrese correo valido")])
    

class FigurasForm(Form):
    figura = RadioField('Figura', 
        choices=[
            ('cua', 'Cuadrado'),
            ('tri', 'Triángulo'), 
            ('cir', 'Círculo'),
            ('pent', 'Pentágono') 
        ],
        validators=[validators.DataRequired(message="Seleccione una figura")]
    )

    valor1 = FloatField('Valor 1', [validators.DataRequired(message="Valor 1 es obligatorio")])
    valor2 = FloatField('Valor 2', default=0.0)