from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.secret_key = 'ioafhwa97e9032iakdnwi'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///penulis.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


from app import routes
db.create_all()


