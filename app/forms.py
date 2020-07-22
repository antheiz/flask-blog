from flask_wtf import FlaskForm
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed
from flask_ckeditor import CKEditorField
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from .models import User

class RegisterForm(FlaskForm):
    username = StringField('username ', validators=[DataRequired(), Length(min=4, max=20, message='username minimal 4 huruf') ])
    email = StringField('email ', validators=[DataRequired(),Email('email salah, silakan periksa kembali') ])
    password = PasswordField('password ', validators=[DataRequired()])
    repeat_password = PasswordField('repeat_password ', validators=[DataRequired(), EqualTo('password', message='password salah')])
    submit = SubmitField('Daftar')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('email telah terpakai, mohon cari yg lain')

class LoginForm(FlaskForm):
    email = StringField('email ', validators=[DataRequired(),Email('email salah, silakan periksa kembali') ])
    password = PasswordField('password ', validators=[DataRequired()])
    remember = BooleanField('ingat saya', default=False)
    submit = SubmitField('Masuk')

class AccountForm(FlaskForm):
    email = StringField('email ', validators=[DataRequired(),Email('email salah, silakan periksa kembali') ])
    username = StringField('username ', validators=[DataRequired(), Length(min=4, max=20, message='username minimal 4 huruf') ])
    picture = FileField('Change Profile', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Simpan')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(f'email {email.data} telah terpakai')
 
class PostForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    content = CKEditorField('content', validators=[DataRequired()])
    # content = TextAreaField('content', validators=[DataRequired()])
    submit = SubmitField('Publish')

class RequestResetForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first.')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')