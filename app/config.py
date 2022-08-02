
class Config:
    SECRET_KEY = '201y3u021jildajwsiawow8'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///flaskblog.db'
        #SQLALCHEMY_DATABASE_URI = 'mysql://theis:salupa@localhost/flaskblog2'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    CKEDITOR_HEIGHT = 600
    CKEDITOR_WIDTH = 1200
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'email'
    MAIL_PASSWORD = 'password'