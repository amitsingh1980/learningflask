from Flask-WTF import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
    Name = StringField('Name', validators=[DataRequired("Please enter your Name")])
    Email = StringField('Email', validators=[DataRequired("Please enter your Email"), Email("Please enter valid email address")])
    Address = StringField('Address', validators=[DataRequired("Please enter your Address")])
    submit = SubmitField('Sign Up')

class LoginForm(Form):
    Email = StringField('Email', validators=[DataRequired("Please enter your email address"), Email("Please enter valid email address")])
    submit = SubmitField('Log In')    

class AddressForm(Form):
    Address = StringField('Address', validators=[DataRequired("Please enter valid address"), Length(min=5,  max=50, message="Please enter valid address between 5 and 50 characters.")])
    submit = SubmitField('Search')

    