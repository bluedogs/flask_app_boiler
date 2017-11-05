# Debug mode
DEBUG = True

# Name of the app
APP_NAME = 'app'

# SQLite DB info
SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}.db'.format(APP_NAME)
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Threads
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"

