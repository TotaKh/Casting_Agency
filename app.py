#----------------------------------------------------------------------------#
# Imports

import os
from flask import Flask, request, abort, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import setup_db, Actors, Movies
from auth import AuthError, requires_auth


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
  def hello():
    return render_template('index.html')


  #---------------
  # Actors endpoint

  @app.route('/actors', methods=['GET'])
  @requires_auth('get:actor')
  def get_actors(jwt):
    ''' 
    GET for all available Actors
    '''
    actors = Actors.query.all()
    
    if len(actors) == 0:
      abort(404)
   
    return jsonify({
      'success': True,
      'total_actors': len(actors),
      'actors': [actor.format() for actor in actors]
    })  
  

  @app.route('/actors', methods=['POST'])
  @requires_auth('post:actor')
  def add_actor(jwt):
    '''
    POST endpoint to craete new actors which require actor name, age and gender 
    '''
    body = request.get_json()

    name = body.get('name')
    age = body.get('age')
    gender = body.get('gender')

    if name == '':
      abort(422)

    try:
      actor = Actors(name=name, age=age, gender=gender)
      actor.insert()

      return jsonify({
        'success': True,
        'created': actor.format()
      })

    except:
      abort(422)

  
  @app.route('/actors/<int:actor_id>', methods=['PATCH'])
  @requires_auth('patch:actor')
  def update_actor(jwt, actor_id):

    body = request.get_json()
    name = body.get('name')
    age = body.get('age')
    gender = body.get('gender')

    actor = Actors.query.filter(Actors.id == actor_id).one_or_none()

    if actor is None:
      abort(404)

    try:
      actor.name = name
      actor.age = age
      actor.gender = gender
      actor.update()

      return jsonify({
          "success": True,
          "update actor": actor.format()
        })

    except:
      abort(422)


  @app.route('/actors/<int:actor_id>', methods=['DELETE'])
  @requires_auth('delete:actor')
  def delete_actor(jwt, actor_id):
    '''
    An endpoint to DELETE actor using ID. 
    '''
    actor = Actors.query.filter(Actors.id == actor_id).one_or_none()
    if actor is None:
      abort(422)
    
    actor.delete()

    return jsonify({
      'success': True,  
      'deleted': actor_id    
    })


  #-----------------
  # Movies endpoint

  @app.route('/movies', methods=['GET'])
  @requires_auth('get:movie')
  def get_movies(jwt):
    ''' 
    GET for all available Movies
    '''
    movies = Movies.query.all()
    
    if len(movies) == 0:
      abort(404)
    
    return jsonify({
      'success': True,
      'total_movies': len(movies),      
      'movies': [movie.format() for movie in movies]
    })  


  @app.route('/movies', methods=['POST'])
  @requires_auth('post:movie')
  def add_movie(jwt):
    '''
    POST endpoint to craete new movies which require movie title , release year and main actor
    '''
    body = request.get_json()
    title = body.get('title')
    release = body.get('release')
    actor = body.get('actor')


    if (title == ''):
      abort(422)

    try:
      movie = Movies(title=title, release=release, actor=actor)
      movie.insert()

      return jsonify({
        'success': True,
        'created': movie.format()
      })

    except:
      abort(422)


  @app.route('/movies/<int:movie_id>', methods=['PATCH'])
  @requires_auth('patch:movie')
  def update_movie(jwt, movie_id):

    body = request.get_json()
    title = body.get('title')
    release = body.get('release')
    actor = body.get('actor')

    movie = Movies.query.filter(Movies.id == movie_id).one_or_none()

    if movie is None:
      abort(404)

    try:
      movie.title = title
      movie.release = release
      movie.actor = actor
      movie.update()

      return jsonify({
          "success": True,
          "update movie": movie.format()
        })

    except:
      abort(422)


  @app.route('/movies/<int:movie_id>', methods=['DELETE'])
  @requires_auth('delete:movie')
  def delete_movie(jwt, movie_id):
    '''
    An endpoint to DELETE movie using ID. 
    '''
    movie = Movies.query.filter(Movies.id == movie_id).one_or_none()
    if movie is None:
      abort(422)
    
    movie.delete()

    return jsonify({
      'success': True,  
      'deleted': movie_id    
    })


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

  
  #error handler for AuthError to conform to general task above
  @app.errorhandler(AuthError)
  def not_authenticated(auth_error):
    return jsonify({
      "success": False,
      "error": auth_error.status_code,
      "message": auth_error.error
    }), 401


  return app


app = create_app()

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)


