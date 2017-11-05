from flask import Blueprint, render_template

home = Blueprint('home', __name__)

# Basic site routes
@home.route('/')
def index():
    # future blog posts (add 'posts=posts' for Jinja2 variable)
    # posts = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()

    return render_template('index.html')

@home.route('/about')
def about():
    # Add the about page
    return render_template('about.html')

@home.route('/contact')
def contact():
    # Add a contact form
    return render_template('contact.html')
