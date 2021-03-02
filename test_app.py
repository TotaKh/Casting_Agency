import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actors, Movies


Producer_token = {'Authorization': 'Bearer {}'.format(os.getenv('PRODUCER_TOKEN'))}
Director_token = {'Authorization': 'Bearer {}'.format(os.getenv('DIRECTOR_TOKEN'))}
Assistant_token = {'Authorization': 'Bearer {}'.format(os.getenv('ASSISTANT_TOKEN'))}


class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "Casting_Agency_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', "Casting_Agency_test")
        setup_db(self.app, self.database_path)


        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    
    #Test for successful operation and for expected errors.
    #--------------------------------------------------------------------------------
    # test Actor endpoints 
    #   get Actor
    def test_200_get_Actor_Assistant(self):
        res = self.client().get('/actors', headers=Assistant_token)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True) 
        self.assertTrue(data['total_actors'])
        self.assertTrue(data['actors'])

    #   post Actor
    def test_200_post_Actor_Director(self):
        res = self.client().post('/actors', headers=Director_token, json={'name':'actor100'})# id is 11
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True) 
        self.assertTrue(data['created'])

    def test_422_post_Actor_Director(self):
        res = self.client().post('/actors', headers=Director_token, json={'name':''})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    #   patch Actor
    def test_200_patch_Actor_Director(self):
        res = self.client().patch('/actors/11', headers=Director_token, json={'name':'Actor'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True) 
        self.assertTrue(data['update actor'])

    def test_404_patch_Actor_Director(self):
        res = self.client().patch('/actors/1000', headers=Director_token, json={'name':'Actor'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False) 
        self.assertEqual(data['message'], 'resource not found')


    #   delete Actor
    def test_200_delete_Actor_Director(self):
        res = self.client().delete('/actors/11', headers=Director_token)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True) 
        self.assertTrue(data['deleted'])

    def test_422_delete_Actor_Director(self):
        res = self.client().delete('/actors/1000', headers=Director_token)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False) 
        self.assertEqual(data['message'], 'unprocessable')
  
    #--------------------------------------------------------------------------------
    # test Movie endpoints 
    #   get Movie
    def test_200_get_Movie_Assistant(self):
        res = self.client().get('/movies', headers=Assistant_token)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True) 
        self.assertTrue(data['total_movies'])
        self.assertTrue(data['movies'])

    #   post Movie
    def test_200_post_Movie_Producer(self):
        res = self.client().post('/movies', headers=Producer_token ,json={'title':'movie'})# id is 11
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True) 
        self.assertTrue(data['created'])
    
    def test_422_post_Movie_Producer(self):
        res = self.client().post('/movies', headers=Producer_token ,json={'title':''})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False) 
        self.assertEqual(data['message'], 'unprocessable')

    #   patch Movie
    def test_200_patch_Movie_Director(self):
        res = self.client().patch('/movies/11', headers=Director_token ,json={'title':'movie'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True) 
        self.assertTrue(data['update movie'])
    
    def test_404_patch_Movie_Director(self):
        res = self.client().patch('/movies/1000', headers=Director_token ,json={'title':'movie'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False) 
        self.assertEqual(data['message'], 'resource not found')

    #   delete Movie
    def test_200_delete_Movie_Producer(self):
        res = self.client().delete('/movies/11', headers=Producer_token)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True) 
        self.assertTrue(data['deleted'])
    
    def test_422_delete_Movie_Producer(self):
        res = self.client().delete('/movies/1000', headers=Producer_token)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False) 
        self.assertEqual(data['message'], 'unprocessable')


  
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()