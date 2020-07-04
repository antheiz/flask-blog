from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegisterForm(FlaskForm):
    username = StringField('Username ', validators=[DataRequired(), Length(min=4, max=20) ])
    email = StringField('Email ', validators=[DataRequired(),Email('Email Failed, Please check your Email') ])
    password = PasswordField('Password ', validators=[DataRequired()])
    repeat_password = PasswordField('Repeat Password ', validators=[DataRequired(), EqualTo('password', message='Password Failed, Please check your Password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email ', validators=[DataRequired(),Email('Email Failed, Please check your Email') ])
    password = PasswordField('Passowrd ', validators=[DataRequired()])
    remember = BooleanField('Remember me', default=False)
    submit = SubmitField('Sign in')
    
