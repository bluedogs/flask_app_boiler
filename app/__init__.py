# Import the Flask basics
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config

import logging
logger = logging.getLogger(__name__)

# Define the App
app = Flask(__name__)
app.config.from_object(config)

# Define the DB
db = SQLAlchemy(app)

# Migrate DB to fix any changes
migrate = Migrate(app, db)

# Setup a Flask-Login Manager
login_manager = LoginManager(app)

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

# Build the DB
db.create_all()





