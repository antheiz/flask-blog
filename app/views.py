from app import app
from flask import render_template, url_for, redirect, url_for, flash
from .forms import RegisterForm, LoginForm

posts = [
    {
        'penulis':'Theis',
        'judul':'postingan pertama',
        'isi':'Ini postingan pertama',
        'date_post':'Juni 28, 2020',
    },
    {
        'penulis':'Jhon',
        'judul':'postingan kedua',
        'isi':'Ini postingan kedua',
        'date_post':'Juni 28, 2020',
    }
]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', judul='About')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'Success account {{form.username.data}} created', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


