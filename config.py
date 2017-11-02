# Debug mode
DEBUG = True

# Name of the app
APP_NAME = 'app'

# App dir
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# SQLite DB info
SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}.{1}.db'.format(BASE_DIR, APP_NAME)
DATABASE_CONNECTION_OPTIONS = {}

# Threads
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"

