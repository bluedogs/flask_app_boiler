# Basic Flask imports
from flask import Blueprint, render_template, \
                    flash, g, session, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user

import logging
logger = logging.getLogger(__name__)

# import the app
from app import db

# import the auth components
from app.auth.forms import LoginForm, RegisterForm, ResetPasswordForm
from app.auth.models import User

# define the auth Blueprint
auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    Handle requests to the /signup route
    Add an user to the database through the registration form
    """
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        # Add a check for specific email domain
        # dumb trick
        if email.endswith('@example.com'):
            user = User(email=form.email.data,
                        name=form.name.data,
                        password=form.password.data)
            user.is_admin = False

            # add user to the database
            db.session.add(user)
            db.session.commit()
            flash('You have successfully registered! You may now login.')

            # redirect to the login page
            return redirect(url_for('auth.signin'))
        else:
            # redirect to the login page as the email domain does not match
            flash("Sorry, We are not accepting users at this time.")
            return redirect(url_for('home.index'))

    # load registration template
    return render_template('auth/signup.html', form=form)

@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    """
    Handle requests to the /signin route
    Log an user in through the signin form
    """
    form = LoginForm()
    if form.validate_on_submit():

        # check whether user exists in the database and whether
        # the password entered matches the password in the database
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            # log user in
            login_user(user)

            # redirect to the dashboard page after login
            return redirect(url_for('home.index'))

        # when login details are incorrect
        else:
            flash('Invalid email or password.')

    # load login template
    return render_template('auth/signin.html', form=form)

@auth.route('/signout')
def signout():
    """
    Handle requests to the /logout route
    Log an user out through the logout link
    """
    # Redirect users who are not logged in.
    if not current_user or current_user.is_anonymous:
        return redirect(url_for('auth.signin'))
    logout_user()
    flash('You have successfully been signed out.')

    # redirect to the login page
    return redirect(url_for('auth.signin'))

@auth.route('/profile')
def profile():

    # Redirect users who are not logged in.
    if not current_user or current_user.is_anonymous:
        return redirect(url_for('auth.signin'))
    return render_template('auth/profile.html')

@auth.route('/forgot', methods=['GET', 'POST'])
def forgot():

    return render_template('auth/forgot.html')


@auth.route('/passwordreset', methods=['GET', 'POST'])
def passwordreset():
    """
    Handle requests to the /passwordreset route
    Update users password
    """

    # Redirect users who are not logged in.
    if not current_user or current_user.is_anonymous:
        return redirect(url_for('auth.signin'))

    form = ResetPasswordForm()

    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        user.password = form.password.data

        # add user to the database
        db.session.add(user)
        db.session.commit()

        logout_user()

        flash('You have successfully reset your password. Please signin.')

        # redirect to the login page
        return redirect(url_for('auth.signin'))

    return render_template('auth/reset.html', form=form)

