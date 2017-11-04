# Import the Flask basics
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import config

# Define the App
app = Flask(__name__)
app.config.from_object(config)

# Define the DB
db = SQLAlchemy(app)

# Basic site routes
@app.route('/')
def index():
	# future blog posts (add 'posts=posts' for Jinja2 variable)
    # posts = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()

    return render_template('index.html')

@app.route('/about')
def about():
	# Add the about page
    return render_template('about.html')
       
@app.route('/contact')
def contact():
	# Add a contact form 
    return render_template('contact.html')

#
# Module Imports
#

# Import the module / component using their blueprints
from app.mod_auth.controllers import mod_auth as auth_module

# Register Blueprints
app.register_blueprint(auth_module)
# app.register_blueprint(random_module)

# Build the DB
db.create_all()
