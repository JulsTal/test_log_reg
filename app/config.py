import os
from flask_sqlalchemy import SQLAlchemy
class Config(object):
   SQLALCHEMY_DATABASE_URI ='sqlite:///users.sqlite3'
   SECRET_KEY='apple key'
   SQLALCHEMY_TRACK_MODIFICATIONS = True