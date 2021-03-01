# Full Stack Project

## Introduction




## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


#### PIP Dependencies

Install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.


#### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 


#### Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:

```bash
dropdb ..
createdb ..
psql .. < ...psql
```

#### Running the server

From within the `backend` directory first ensure you are working using your created virtual environment. Base URL is: http://127.0.0.1:5000/

To run the server naviging to the `/backend` directory, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 




## Errors

Errors status codes that could occur when requests fail:

- 400 (Bad Request)
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
To run the tests naviging to the `/backend` directory and running:
```
dropdb ..
createdb ..
psql .. < ...psql
python ...py
```

## API Endpoints 

List of all endpoints in the project:

1. 


