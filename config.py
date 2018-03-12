# Statement for enabling the development environment
DEBUG = True

# secret key
SECRET_KEY = 'Super secret key'

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - woring with SQLite
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'catalog.db')
DATABASE_CONNECT_OPTIONS = {}

import json
CLIENT_ID = json.loads(
    open(os.path.join(BASE_DIR, 'client_secrets.json'), 'r').read()
)['web']['client_id']
