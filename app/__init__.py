# Import the Flask basics
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import config

# Define the App
app = Flask(__name__)
app.config.from_object(config)

# Define the DB
db = SQLAlchemy(app)

# Handle 404's with style
@app.errorhandler(404)
def not_found():
    return render_template('404.html'), 404

# Import the module / component using their blueprints
from app.mod_auth.controllers import mod_auth as auth_module

# Register Blueprints
app.register_blueprint(auth_module)
# app.register_blueprint(random_module)

# Build the DB
db.create_all()
