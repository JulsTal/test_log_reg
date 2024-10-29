from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from .config import Config
# Инициализация Flask приложения
app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)

# Инициализация SQLAlchemy и Bcrypt
users = SQLAlchemy(app)
bcrypt = Bcrypt(app)
users.create_all()
