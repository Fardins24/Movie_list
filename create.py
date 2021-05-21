from app import db
from application.models import User, Movie
db.drop_all()
db.create_all()

user = User(
    first_name ='Bill',
    last_name = 'Bob',
    age = 26
    )

movie = Movie(
    movie_name ='Avengers',
    movie_genre = 'Action'
    )

db.session.add(user)
db.session.add(movie)

db.session.commit()