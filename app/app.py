from flask import Flask
from . import app, users
from .views import index

from .models import News, Users
with app.app_context():
    users.create_all()
if __name__ == "__main__":
    app.run(debug=True)

