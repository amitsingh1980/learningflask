from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
    Name = StringField('Name', validators=[DataRequired("Please enter your Name")])
    Email = StringField('Email', validators=[DataRequired("Please enter your Email"), Email("Please enter valid email address")])
    Address = StringField('Address', validators=[DataRequired("Please enter your Address")])
    submit = SubmitField('Sign Up')