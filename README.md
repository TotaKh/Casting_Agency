# Full Stack Capstone Project - Casting Agency

## Introduction

This is the last project in Full Stack nanodegree I learned a lot with Udacity and I enjoyed applying everything I learned in this project, I feel good to what I have accomplished.

## Casting Agency
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. creating a system to simplify and streamline the process for all of company members.
The system can:
1. Retrieve data for both actors and movies
2. Inserting a new actor or movie into the database
3. Modify the data of both actors and films
4. Delete an actor or movie from the database

### hosted on ...


### Authentication
There are 3 roles for system users each of them has permissions. 
These are their login information:

1. Executive Producer
```bash
email: ExecutiveProducer@agency.com
password: Qwer1234
```
-  Can view actors and movies
    - `get:actor`
    - `get:movie`
-  Add or delete an actor from the database
    - `post:actor`
    - `delete:actor`
- Add or delete a movie from the database
    - `post:movie`
    - `delete:movie`
-  Modify actors or movies
    - `patch:actor`
    - `patch:movie`


2. Casting Director
```bash
email: Director@agency.com
password: Qwer1234
```
-  Can view actors and movies
    - `get:actor`
    - `get:movie`
-  Add or delete an actor from the database
    - `post:actor`
    - `delete:actor`
-  Modify actors or movies
    - `patch:actor`
    - `patch:movie`


3. Casting Assistant
```bash
email: Assistant@agency.com
password: Qwer1234
```
-  Can view actors and movies
    - `get:actor`
    - `get:movie`


## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by execute:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.


#### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.


#### Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:

```bash
dropdb Casting_Agency
createdb Casting_Agency
psql Casting_Agency < Casting_Agency.psql
```

#### Running the server
From within the directory first ensure you are working using your created virtual environment. Base URL is: http://127.0.0.1:5000/

To run the server execute:

```bash
export FLASK_APP=app
export FLASK_DEBUG=True
export FLASK_ENVIRONMENT=debug
flask run --reload
```

Setting the `FLASK_APP` variable to `app` file and find the application. 

The `--reload` flag will detect file changes and restart the server automatically.



## Errors

Errors status codes that could occur when requests fail:

- 400 (Bad Request)
- 401 (Unauthorized)
- 403 (Forbidden response)
- 404 (resource not found)
- 405 (method not allowed)
- 422 (unprocessable)
- 500 (internal server error)

Errors return JSON with the following format:
```
{
  "error": 404, 
  "message": "resource not found", 
  "success": false
}
```

### Testing
#### Test using unitests
This test focuses on different aspects of the success and failure of each endpoint.
To run the tests and execute:
```
dropdb Casting_Agency_test
createdb Casting_Agency_test
psql Casting_Agency_test < Casting_Agency.psql
python3 .py
```

#### Test using Postman
This test focuses on authentication and permissions for each role.
[Postman](https://getpostman.com)
- Import the postman collection ` test_casting_agency`
- Run the collection.

---------------------------

## API Endpoints 

List of all endpoints in the project:

1. 


