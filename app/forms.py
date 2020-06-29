from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class RegisterForm(FlaskForm):
    username = StringField('Username ', validators=[DataRequired(), Length(min=4, max=20, message='Username minimal 4 Huruf dan maksimal 20')])
    email = StringField('Email ', validators=[DataRequired(), Email('Format email Salah')])
    password = PasswordField('Password ', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm_password', validators=[DataRequired(), EqualTo('password', message='password salah')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email ', validators=[DataRequired(), Email('Format email Salah')])
    password = PasswordField('Password ', validators=[DataRequired()])
    remember = BooleanField('Remember me', default=False)
    submit = SubmitField('Sign In')
