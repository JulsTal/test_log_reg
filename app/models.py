from datetime import datetime
from . import users
from flask_login import UserMixin
class Users(users.Model, UserMixin):
    __tablename__="users"
    id=users.Column(users.Integer, primary_key=True)
    username=users.Column(users.String(20), nullable=False, unique=True)
    password=users.Column(users.String(80), nullable=False)
class News(users.Model):
    __tablename__="news"
    id_news=users.Column(users.Integer,primary_key=True)
    name=users.Column(users.String(100), nullable=False)
    text_news=users.Column(users.Text, nullable=False)
    url=users.Column(users.Text, nullable=False)
    created_on=users.Column(users.DateTime, default=datetime.utcnow)



