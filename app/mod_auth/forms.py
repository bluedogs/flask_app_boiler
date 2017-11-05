from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, BooleanField, StringField
from wtforms.validators import Required, Email, EqualTo, InputRequired, Length

class LoginForm(FlaskForm):
    """ Define the Login Form """
    email = TextField('Email Address', [Email(),
            Required(message='Forgot to enter email address?')])
    password = PasswordField('Password', [
            Required(message='Please supply a password.')])

class RegisterForm(FlaskForm):

    name_message = "Your name is too long."
    email_message = "Your email is too long."
    pass_message = "Your password is too short (under 8 characters), please choose another."
    
    name = StringField('name', 
        validators=[
        InputRequired(), 
        Length(max=64)
        ]
        ) 
    email = StringField('email', 
        validators=[
        InputRequired(), 
        Email(message='Invalid email'), 
        Length(max=64, message=email_message)
        ]
        )
    password = PasswordField('password', 
        validators=[
        InputRequired(), 
        Length(min=8, message=pass_message)
        ]
        )