import os
from sqlalchemy import Column, String, Integer, ForeignKey, create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json

# gh jksd jpctd vh 
#database_path = os.environ['DATABASE_URL']
database_path='postgresql://taghreed:122333@localhost:5432/Casting_Agency'

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
  app.config["SQLALCHEMY_DATABASE_URI"] = database_path
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
  db.app = app
  db.init_app(app)
  migrate = Migrate(app, db)
  db.create_all()


'''
Movies
Have title and release year
'''
class Movies(db.Model):  
  __tablename__ = 'movies'

  id = Column(Integer, primary_key=True)
  title = Column(String)
  release = Column(String)
  actor = Column(String , ForeignKey('actors.name'))

  def __init__(self, title, release='' ,actor='' ):
    self.title = title
    self.release = release
    self.actor = actor

  def insert(self):
    db.session.add(self)
    db.session.commit()

  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()


  def format(self):
    return {
      'id': self.id,
      'title': self.title,
      'release': self.release,
      'actor':self.actor
    }


'''
Actors
Have name, age and gender
'''
class Actors(db.Model):
  __tablename__ = 'actors'

  id = Column(Integer, primary_key=True)
  name = Column(String , unique=True)
  age = Column(Integer)
  gender = Column(String)
  movie = db.relationship('Movies' , backref='movie', lazy=True)

  def __init__(self, name, age='', gender='' ):
    self.name = name
    self.age = age
    self.gender = gender

  def insert(self):
    db.session.add(self)
    db.session.commit()

  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'age': self.age,
      'gender': self.gender
      }