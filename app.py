#----------------------------------------------------------------------------#
# Imports

import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Actors, Movies


#----------------------------------------------------------------------------#
# App Config.

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)

  # Use the after_request decorator to set Access-Control-Allow
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization ,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, OPTIONS, DELETE')
    return response


  #----------------------------------------------------------------------------#
  #  Endpoint

  @app.route('/')
  def hi():
    return "hello world"


  #---------------
  # Actors endpoint

  @app.route('/actors', methods=['GET'])
  def get_actors():
    ''' 
    GET for all available Actors
    '''
    actors = Actors.query.all()
    
    if actors == 0:
      abort(404)
   
    return jsonify({
      'success': True,
      'actors': [actor.format() for actor in actors]
    })  
  

  @app.route('/actors', methods=['POST'])
  def add_actor():
    '''
    POST endpoint to craete new actors which require actor name, age and gender 
    '''
    
    body = request.get_json()

    name = body.get('name')
    age = body.get('age')
    gender = body.get('gender')

    if (name == ''):
      abort(422)

    try:
      actor = Actors(name=name, age=age, gender=gender)
      actor.insert()

      return jsonify({
        'success': True,
        'created': actor.id,
      })

    except:
      abort(422)

  #---------------
  # Movies endpoint

  @app.route('/movies', methods=['GET'])
  def get_movies():
    ''' 
    GET for all available Movies
    '''
    movies = Movies.query.all()
    
    if movies == 0:
      abort(404)
    
    return jsonify({
      'success': True,
      'movies': [movies.format() for movie in movies]
    })  


    @app.route('/movies', methods=['POST'])
    def add_movie():
      '''
      POST endpoint to craete new movies which require movie title , release year and main actor
      '''
      
      body = request.get_json()

      title = body.get('title')
      release = body.get('release')
      actor = body.getlist('actor')


      if (title == ''):
        abort(422)

      try:
        movie = Actors(title=title, release=release)
        movie.insert()

        return jsonify({
          'success': True,
          'created': movie.id,
        })

      except:
        abort(422)


  #----------------------------------------------------------------------------#
  # Error Handlers.
  
  @app.errorhandler(400)
  def Bad_Request(error):
    return jsonify({
      'success': False,
      'error': 400,
      'message': "Bad Request"
    }),400

  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      'success': False,
      'error': 404,
      'message': "resource not found"
    }),404

  @app.errorhandler(405)
  def not_found(error):
    return jsonify({
      'success': False,
      'error': 405,
      'message': "method not allowed"
    }),405

  @app.errorhandler(422)
  def Unprocessable(error):
    return jsonify({
      'success': False,
      'error': 422,
      'message': "unprocessable"
    }),422

    @app.errorhandler(500)
    def exception_handler(error):
      return jsonify({
        'success': False,
        'error': 500,
        'message': "internal server error"
      }), 500

  return app

app = create_app()

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)



# Models:

# Movies with attributes title and release date
# Actors with attributes name, age and gender

# Endpoints:
# GET /actors and /movies
# DELETE /actors/ and /movies/
# POST /actors and /movies and
# PATCH /actors/ and /movies/

# Roles:
# Casting Assistant
# Can view actors and movies
# Casting Director
# All permissions a Casting Assistant has and…
# Add or delete an actor from the database
# Modify actors or movies
# Executive Producer
# All permissions a Casting Director has and…
# Add or delete a movie from the database