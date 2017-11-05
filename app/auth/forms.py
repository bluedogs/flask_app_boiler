from flask_wtf import FlaskForm
from wtforms import StringField, TextField, PasswordField, validators


class LoginForm(FlaskForm):
    """ Define the Login Form """
    email = TextField('Email Address', [validators.Email(),
            validators.DataRequired(message='Forgot to enter email address?')])
    password = PasswordField('Password', [
            validators.DataRequired(message='Please supply a password.')])

class RegisterForm(FlaskForm):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')