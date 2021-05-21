from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.fields.core import IntegerField
from wtforms.validators import DataRequired

from application.models import Movie

class MovieForm(FlaskForm):

    movie_name = StringField('Movie Name',
        validators = [
            DataRequired()
        ]
    )
    movie_genre = StringField('Movie Genre',
        validators = [
            DataRequired()
        ]
    )
    submit = SubmitField('Submit')

class UserForm(FlaskForm):

   
    first_name = StringField('First Name',
        validators = [
            DataRequired()
        ] )
    
    last_name = StringField('Last Name',
        validators = [
            DataRequired()
        ] )
    
    age = IntegerField('Age',
        validators = [
            DataRequired()
        ] )


    submit = SubmitField('Submit')

    
