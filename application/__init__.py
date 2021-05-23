from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@35.242.141.175:3306/movie_list"
app.config['SECRET_KEY'] = getenv("SECRETKEY")

db = SQLAlchemy(app)

from application import routes 