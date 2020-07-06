from app import app, db, bcrypt
from flask import render_template, redirect, url_for, flash
from app.models import User, Post
from .forms import RegisterForm, LoginForm

@app.route('/', methods=['get','post'])
def index():
    judul = 'Flask | Home'
    return render_template ('index.html',judul=judul)

@app.route('/about')
def about():
    judul = 'Flask | About'
    return render_template('about.html', judul=judul)

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
        hash_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hash_pw)
        db.session.add(user)
        db.session.commit()
        flash('Account has been create, Please','success')                  
    return render_template ('register.html', form=form ,judul=judul)
