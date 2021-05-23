from application import app, db
from flask import render_template, url_for, redirect, request
from application.forms import MovieForm, UserForm
from application.models import Movie, User


@app.route('/')
@app.route('/home')
def home():
    all_users = User.query.all()
    return render_template('index.html', all_users=all_users)

@app.route('/create' , methods=['GET', 'POST'])
def create():
    form = UserForm()
    if request.method=='POST':
        if form.validate_on_submit():
            user = User(
                first_name = form.first_name.data,
                last_name = form.last_name.data,
                age = form.age.data
            )
            db.session.add(user)
            db.session.commit()
        return redirect(url_for('home')) 
    return render_template('create.html', subheading= "Create User :)", form=form)

@app.route("/<int:userID>/movie-list")
def movieList(userID):
    movies_list = Movie.query.filter_by(user_id=userID) 
    return render_template ('movieList.html', subheading= "List of Movies", movies_list=movies_list, userID=userID)

    
@app.route("/<int:userID>/movie-list/add" , methods=['GET', 'POST'])
def addMovie(userID):
    form = MovieForm()
    if form.validate_on_submit():
        movie = Movie(
            movie_name = form.movie_name.data,
            movie_genre = form.movie_genre.data,
            user_id = userID 
        )
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for('movieList', userID=userID))
    return render_template('addMovie.html', subheading="Add Movie", form=form)


@app.route("/<int:userID>/movie-list/update/<int:movieID>" , methods=['GET', 'POST'])
def update(userID, movieID):
    form = MovieForm()
    movie = Movie.query.filter_by(id=movieID).first()
    if request.method == 'GET': 
        form.movie_name.data = movie.movie_name
        form.movie_genre.data = movie.movie_genre
    
    elif request.method == "POST": 
        movie.movie_name = form.movie_name.data
        movie.movie_genre = form.movie_genre.data
        db.session.commit()
        return redirect(url_for('movieList', userID=userID))
    return render_template('update.html', subheading="Update Page", movie=movie, userID=userID, form=form)

@app.route("/<int:userID>/movie-list/delete/<int:movieID>" , methods=['GET', 'POST'])
def delete(userID, movieID):
    movie = Movie.query.filter_by(id=movieID).first()
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('movieList', userID=userID))


