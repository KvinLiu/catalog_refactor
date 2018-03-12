from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

from controllers.crud_view import *
from controllers.auth_view import *
from controllers.api_view import *

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
