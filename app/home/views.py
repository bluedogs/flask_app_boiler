from flask import Blueprint, render_template
from flask_login import login_required

import logging
logger = logging.getLogger(__name__)

home = Blueprint('home', __name__)


# Basic site routes
@home.route('/')
def index():
    return render_template('index.html')

@home.route('/about')
def about():
    return render_template('about.html')

@home.route('/contact')
def contact():
    return render_template('contact.html')

@home.route('/test')
@login_required
def test():
    # Just a test page

    return render_template('test.html')
