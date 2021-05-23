from os import name
import unittest
from flask import url_for
from flask.wrappers import Response
from flask_testing import TestCase

from application import app, db 
from application.models import User, Movie


class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            SECRET_KEY='TEST_SECRET_KEY',
            DEBUG=True,
            WTF_CSRF_ENABLED= False
            )
        return app

    def setUp(self):   
            db.create_all()
            test_user= User(
                first_name = "Fardin", 
                last_name = "Shah",
                age = 26 
            )
            test_movie = Movie(
                movie_name = "King Kong",
                movie_genre = "Action"
            )
            test_user.movies.append(test_movie)
            db.session.add(test_user) 
            db.session.add(test_movie)
            db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
   
    def test_create_get(self):
        response = self.client.get(url_for('create'))
        self.assertEqual(response.status_code, 200)

    def test_movieList_get(self):
        response = self.client.get(url_for('movieList', userID=1))
        self.assertEqual(response.status_code, 200)

    def test_addMovie_get(self):
        response = self.client.get(url_for('addMovie', userID=1))
        self.assertEqual(response.status_code, 200)

    def test_update_get(self):
        response = self.client.get(url_for('update', userID=1, movieID=1))
        self.assertEqual(response.status_code, 200)

    def test_delete_get(self):
        response = self.client.get(url_for('delete', userID=1, movieID=1))
        self.assertEqual(response.status_code, 302)

class TestRead(TestBase):
    def test_read_user(self):
        response= self.client.get(url_for("home"))
        self.assertIn(b"Fardin", response.data)  
        self.assertIn(b"Shah", response.data) 

    def test_read_movieList(self):
        response = self.client.get(url_for("movieList" , userID=1))
        self.assertIn(b"King Kong", response.data) 
        self.assertIn(b"Action", response.data) 

    def test_read_update(self):
        response = self.client.get(url_for("update" , userID=1, movieID=1))
        self.assertIn(b"King Kong", response.data) 
        self.assertIn(b"Action", response.data) 
        
        
class TestCreate(TestBase):
    def test_create_user(self):
        response = self.client.post(url_for("create"), 
        data = dict(
            first_name = 'Bob',
            last_name = 'Smith', 
            age = '29', 
        ),  
        follow_redirects= True
        )
        self.assertIn(b"Bob", response.data) 
        self.assertIn(b"Smith", response.data) 

    def test_create_addMovie(self):
        response = self.client.post(url_for("addMovie", userID=1), 
        data = dict(
            movie_name = 'Fast5',
            movie_genre = 'Action'
        ),  
        follow_redirects= True
        )
        self.assertIn(b"Fast5", response.data) 
        self.assertIn(b"Action", response.data) 

    def test_create_update(self):
        response = self.client.post(url_for("update", userID=1, movieID=1), 
        data = dict(
            movie_name = 'Fast6',
            movie_genre = 'Action', 
        ),  
        follow_redirects= True
        )
        self.assertIn(b"Fast6", response.data) 
        self.assertIn(b"Action", response.data)

class TestDelete(TestBase):
    def test_delete_movie(self):
        response = self.client.get(url_for("delete", userID=1, movieID=1))
        self.assertNotIn(b"King Kong", response.data) 
        self.assertNotIn(b"Action", response.data) 
        

     


        

    


    