# Import the Flask basics
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate

import logging

# local imports
from config import app_config

# Define the DB
db = SQLAlchemy()

# Add Models from other Blueprints
# This is helps the command 'flask db migrate' to find your new tables

# from app.folder import model

# Setup a Flask-Login Manager
login_manager = LoginManager()


def create_app(config_name):

    # Define the App
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('../config.py')

    Bootstrap(app)
    db.init_app(app)
    login_manager.init_app(app)

    # Migrate DB to fix any changes
    migrate = Migrate(app, db)

    #
    # Module Imports
    #

    # Import the module / component using their blueprints
    from app.home.views import home
    from app.auth.views import auth

    # Register Blueprints
    app.register_blueprint(home)
    app.register_blueprint(auth)

    # app.register_blueprint(random_module)

    # Set up logging
    logFormatStr = '[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s'
    logging.basicConfig(format=logFormatStr, filename="global.log", level=logging.DEBUG)
    formatter = logging.Formatter(logFormatStr, '%m-%d %H:%M:%S')
    fileHandler = logging.FileHandler("summary.log")
    fileHandler.setLevel(logging.DEBUG)
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setLevel(logging.DEBUG)
    streamHandler.setFormatter(formatter)
    app.logger.addHandler(fileHandler)
    app.logger.addHandler(streamHandler)
    app.logger.info("Logging is set up.")

    return app





