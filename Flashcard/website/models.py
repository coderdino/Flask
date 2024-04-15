#Used for database models
#2 database models: for users and notes

from . import db # . accesses __init__.py from website folder
from flask_login import UserMixin
from sqlalchemy.sql import func

class QuestionAnswer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(10000))
    answer = db.Column(db.String(10000))
    questionanswer = db.Column(db.Integer, db.ForeignKey('note.id'))

class Note(db.Model):
    __tablename__ = 'note'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    linkname = db.Column(db.String(10000))
    type = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now()) # Func gets default date and time
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    questions = db.relationship('QuestionAnswer')

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True) # Unique shows that emails are unique
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') #Everytime we create a note it will store here

