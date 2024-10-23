from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from app.config import Config
app = Flask(__name__, template_folder='templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SECRET_KEY']='apple key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config.from_object(Config)
users = SQLAlchemy(app)

bcrypt = Bcrypt(app)









