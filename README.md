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

### hosted on

https://khalawicastingagency.herokuapp.com


### Authentication 
There are 3 roles for system users each of them has permissions. 
These are their login information:

#### 1. Executive Producer
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

You can log in and create your token [here](https://khalawi.us.auth0.com/authorize?audience=Agency&response_type=token&client_id=PwUwrDo6fgOm80xj1XkR0oSdcVlaGcZq&redirect_uri=http://localhost:8080/login
)

#### 2. Casting Director
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



#### 3. Casting Assistant
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


#### Database Setup localy 
to run the API localy comment line 7 on models.py and un comment line 8,9 :

```bash
# database_path = os.environ['DATABASE_URL']
database_name = "Casting_Agency"
database_path = "postgres://{}/{}".format('localhost:5432', database_name)
```

With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:

```bash
dropdb Casting_Agency
createdb Casting_Agency
psql Casting_Agency < Casting_Agency.pgsql
```


#### Running the server
From within the directory first ensure you are working using your created virtual environment. Base URL is: http://127.0.0.1:5000/

To run the server execute:

```bash
export FLASK_APP=app
flask run --reload
```

Setting the `FLASK_APP` variable to `app` file and find the application. 

The `--reload` flag will detect file changes and restart the server automatically.



## Errors

Errors status codes that could occur when requests fail:

- 400 (Bad Request)
- 401 (Unauthorized)
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
psql Casting_Agency_test < Casting_Agency.pgsql
python3 test_app.py
```

#### Test using Postman
This test focuses on authentication and permissions for each role.
[Postman](https://getpostman.com)
- Import the postman collection ` test_casting_agency`
- Run the collection.


## API Endpoints 

List of all endpoints in the project:

1. GET `'/actors'`
2. POST `'/actors'`
3. PATCH `'/actors/<int:actor_id>'`
4. DELETE `'/actors/<int:actor_id>'`
5. GET `'/movies'`
6. POST `'/movies'`
7. PATCH `'/movies/<int:movie_id>'`
8. DELETE `'/movies/<int:movie_id>'`


### 1. GET `'/actors'`
- Retrieve all actors and their info with the total number of actors.
- Request Arguments: None
- Returns: 
```
{
    "actors": [
        {
            "age": 17,
            "gender": "Female",
            "id": 1,
            "name": "Millie Brown"
        },
        {
            "age": 37,
            "gender": "Male",
            "id": 2,
            "name": "Jesse Eisenberg"
        },
        {
            "age": 55,
            "gender": "Male",
            "id": 3,
            "name": "Robert Downey"
        },
        {
            "age": 46,
            "gender": "Male",
            "id": 4,
            "name": "Leonardo DiCaprio"
        }
    ],
    "success": true,
    "total_actors": 4
```

### 2. POST `'/actors'`
- add new actor to the database.
- Request Arguments: 
```
{
    "age": 45,
    "gender": "Female",
    "name": "Angelina Jolie"
}
```
- Returns:
```
"created": {
        "age": 45,
        "gender": "Female",
        "id": 22,
        "name": "Angelina Jolie"
    },
    "success": true
```

### 3. PATCH `'/actors/<int:actor_id>'`
- update a specific actor info.
- Request Arguments: int:actor_id
```
{
    "age": 33,
    "gender": "Female",
    "name": "Blake Lively"
}
```
- Returns:
```
{
    "success": true,
    "update actor": {
        "age": 33,
        "gender": "Female",
        "id": 20,
        "name": "Blake Lively"
    }
}
```

### 4. DELETE `'/actors/<int:actor_id>'`
- delet a specific actor from database.
- Request Arguments: int:actor_id
- Returns:
```
{
    "deleted": 19,
    "success": true
}
```

### 5. GET `'/movies'`
- Retrieve all movies and their info with the total number of movies.
- Request Arguments: None
- Returns: 
```
{
    "movies": [
        {
            "actor": "Millie Brown",
            "id": 1,
            "release": "2020",
            "title": "Enola Holmes"
        },
        {
            "actor": "Jesse Eisenberg",
            "id": 2,
            "release": "2013",
            "title": "Now You See Me"
        },
        {
            "actor": "Robert Downey",
            "id": 3,
            "release": "2008",
            "title": "Iron Man"
        },
        {
            "actor": "Leonardo DiCaprio",
            "id": 4,
            "release": "2013",
            "title": "The Great Gatsby"
        }
    ],
    "success": true,
    "total_movies": 4

```

### 6. POST `'/movies'`
- add new movie to the database.
- Request Arguments: 
```
{
    "title" : "Maleficent",
    "release" : "2019",
    "actor": "Angelina Jolie"
}
```
- Returns:
```
{
    "created": {
        "actor": "Angelina Jolie",
        "id": 15,
        "release": "2019",
        "title": "Maleficent"
    },
    "success": true
}
```

### 7. PATCH `'/movies/<int:movie_id>'`
- update a specific movie info.
- Request Arguments: int:movie_id
```
{
    "title" : "A Simple Favor",
    "release" : 2018,
    "actor": "Blake Lively"
}
```
- Returns:
```
{
    "success": true,
    "update movie": {
        "actor": "Blake Lively",
        "id": 11,
        "release": "2018",
        "title": "A Simple Favor"
    }
}
```

### 8. DELETE `'/movies/<int:movie_id>'`
- delet a specific movie from database.
- Request Arguments: int:movie_id
- Returns:
```
{
    "deleted": 10,
    "success": true
}
```

