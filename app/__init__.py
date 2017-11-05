# Import the Flask basics
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

import logging
logger = logging.getLogger(__name__)

# Define the App
app = Flask(__name__)
app.config.from_object(config)

# Define the DB
db = SQLAlchemy(app)

#
# Module Imports
#

# Import the module / component using their blueprints
from app.home.views import home
from app.auth.views import mod_auth as auth

# Register Blueprints
app.register_blueprint(home)
app.register_blueprint(auth)
# app.register_blueprint(random_module)

# Build the DB
db.create_all()
