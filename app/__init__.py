from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_ckeditor import CKEditor

app = Flask(__name__)
app.secret_key = 'ioafhwa97e9032iakdnwi'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskblog.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://theis:salupa@localhost/flaskblog2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'danger'
ckeditor = CKEditor(app)
app.config['CKEDITOR_HEIGHT'] = 600
app.config['CKEDITOR_WIDTH'] = 1200


from app import routes




