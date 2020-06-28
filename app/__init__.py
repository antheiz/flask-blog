from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'NDeuw5LsA0NCAWYw7iow'

from app import views