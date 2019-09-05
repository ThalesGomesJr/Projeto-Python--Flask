from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(Form):
    usuario = StringField("Usuario", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    