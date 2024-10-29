from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from app.config import Config
app = Flask(__name__, template_folder='templates')


app.config.from_object(Config)
users = SQLAlchemy(app)

bcrypt = Bcrypt(app)









