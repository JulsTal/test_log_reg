from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import config

# Инициализация Flask приложения
app = Flask(__name__, template_folder='templates')
app.config.from_object(config.Config)

# Инициализация SQLAlchemy и Bcrypt
users = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Создание всех таблиц в базе данных
with app.app_context():
    users.create_all()
