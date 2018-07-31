#!/usr/bin/env python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


from config import Config


app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login_page'


from routes import *
# from dbconnect import *


if __name__ == "__main__":
	app.run(debug=True)

