from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError

class RegisterForm(FlaskForm):
    username = StringField('Username :', validators=[DataRequired(), Length(min=2, max=15,message=('Wajib Masukan Nama Minimal 2 Huruf'))])
    email = StringField('Email :', validators=[DataRequired(), Email('Email yang dimasukan salah')])
    password = PasswordField('Password :', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Password tidak Sama')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username :', validators=[DataRequired(), Length(min=2, max=15)])
    password = PasswordField('Password :', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')