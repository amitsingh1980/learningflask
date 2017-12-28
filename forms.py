from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField

class SignupForm(Form):
    Name = StringField('Name')
    Email = StringField('Email')
    submit = SubmitField('Sign Up')