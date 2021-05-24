from app import db
from application.models import User, Movie
db.drop_all()
db.create_all()
