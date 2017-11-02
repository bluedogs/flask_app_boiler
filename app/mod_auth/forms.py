from flask_wtf import Form
from wtforms import TextField, PasswordField, BooleanField
from wtforms.validators import Required, Email, EqualTo

class LoginForm(Form):
    """ Define the Login Form """
    email = TextField('Email Address', [Email(),
            Required(message='Forgot to enter email address?')])
    password = PasswordField('Password', [
            Required(message='Please supply a password.')])
