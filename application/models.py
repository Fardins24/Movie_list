from application import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    movies = db.relationship('Movie', backref='user')

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_name = db.Column(db.String(30), nullable=False)
    movie_genre = db.Column(db.String(30), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)