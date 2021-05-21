from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@35.242.141.175:3306/movie_list"
app.config['SECRET_KEY'] = "Fardin"

db = SQLAlchemy(app)

from application import routes 