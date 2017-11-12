# config.py

import os

class Config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments

    # Name of the app
    APP_NAME = 'app'
    HOST = '127.0.0.1'
    PORT = '5000'

    # SQLite DB info
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, '{0}.db'.format(APP_NAME))

    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(db_path)
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # Threads
    THREADS_PER_PAGE = 2

    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED     = True

    # Use a secure, unique and absolutely secret key for
    # signing the data. Default: MD5 of "secret"
    CSRF_SESSION_KEY = "5ebe2294ecd0e0f08eab7690d2a6ee69"

    # Secret key for signing cookies
    SECRET_KEY = "5ebe2294ecd0e0f08eab7690d2a6ee69"



class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True



class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

