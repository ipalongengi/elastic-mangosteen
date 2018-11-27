from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
app.config.from_pyfile('../instance/config.py')

db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

from . import views, models