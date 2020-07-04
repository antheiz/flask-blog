from app import app
from flask import render_template, redirect, url_for, flash
from .forms import RegisterForm, LoginForm

@app.route('/', methods=['get','post'])
def index():
    judul = 'Flask | Home'
    return render_template ('index.html',judul=judul)


@app.route('/login', methods=['get','post'])
def login():
    judul = 'Flask | Login'
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'theis@gmail.com' and form.password.data == 'a':
            flash(f'Successfull, Welcome','success')
            return redirect(url_for('index'))
        else:
            flash(f'Failed, Please Try Again','danger')            
    return render_template ('login.html', form=form, judul=judul)

@app.route('/register', methods=['get','post'])
def register():
    judul = 'Flask | Register'
    form = RegisterForm()
    if form.validate_on_submit():  
        flash(f'Account has been created!, please', 'success')                           
    return render_template ('register.html', form=form ,judul=judul)
