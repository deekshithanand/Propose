# form validation
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,validators,SubmitField

class LoginForm(FlaskForm):
    
    uname = StringField('User Name ',[validators.DataRequired()])
    pwd = PasswordField('Password ',[validators.DataRequired()])
    
    
class SignUpForm(FlaskForm):
    uname = StringField('User Name',[validators.DataRequired(),validators.Length(min=5,max = 10,message="Username should be between 5 and 10 characters")])
    email = StringField('Email',[validators.Email(message='Invalid email'),validators.DataRequired("Field Required")])
    pwd = PasswordField('Password',[validators.DataRequired(),])
    cpwd = PasswordField('Confirm Password',[validators.DataRequired(),
    validators.EqualTo('pwd',message="Passwords Do not Match"),
    ])
    submit = SubmitField('Signup/Register')
    