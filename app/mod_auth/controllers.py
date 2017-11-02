# Basic Flask imports
from flask import Blueprint, request, render_template, \
                    flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash

# import the app
from app import app
# import the auth components
from app.mod_auth.forms import LoginForm
from app.mod_auth.models import User

# define the auth Blueprint
mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

# Setup the routes
@mod_auth.route('/signin/', methods=['GET', 'POST'])
def signin():
    form = LoginForm(request.form)

    # User Login Session
    if form.validate_on_submit():
        # Check the username
        user = User.query.filter_by(email=form.email.data).first()

        if user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            flash('Welcome {0}'.format(user.name))
            return redirect(url_for('auth.home'))
        flash('Wrong email or password', 'error-message')
    return render_template("auth/signin.html", form=form)

