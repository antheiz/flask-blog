from app import app
from flask import render_template, url_for
# from .forms import RegisterForm, LoginForm

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

