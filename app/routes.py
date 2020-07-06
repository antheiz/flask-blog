from app import app, db, bcrypt
from flask import render_template, redirect, url_for, flash, request
from app.models import User, Post
from .forms import RegisterForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/', methods=['get','post'])
def index():
    return render_template ('index.html',judul='Home')

@app.route('/about')
def about():
    return render_template('about.html', judul='About')

@app.route('/register', methods=['get','post'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():  
        hash_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hash_pw)
        db.session.add(user)
        db.session.commit()
        flash('Account has been create, Please','success')                  
    return render_template ('register.html', form=form ,judul='Register')


@app.route('/login', methods=['get','post'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:            
            flash(f'Failed, Please Try Again','danger')            
    return render_template ('login.html', form=form, judul='Login')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/account')
@login_required
def account():
    return render_template('account.html', judul='Account')