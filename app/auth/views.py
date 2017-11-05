# Basic Flask imports
from flask import Blueprint, request, render_template, \
                    flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash

# import the app
from app import app, db
# import the auth components
from app.auth.forms import LoginForm, RegisterForm
from app.auth.models import User

# define the auth Blueprint
mod_auth = Blueprint('auth', __name__, url_prefix="/auth")

# Setup the routes
@mod_auth.route('/signin/', methods=['GET', 'POST'])
def signin():
    form = LoginForm()
    if request.method == "POST":
        # User Login Session
        if form.validate_on_submit():
            # Check the username
            user = User.query.filter_by(email=request.form['email']).first()

            if user and check_password_hash(user.password, request.form['password']):
                session['username'] = request.form['email']
                flash('Welcome {0}'.format(request.form['email']))
                print(user.email)
                return redirect(url_for('home.index'))
            flash('Wrong email or password', 'error-message')
    return render_template("auth/signin.html", form=form)


@mod_auth.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = RegisterForm(request.form)

    # User Login Session
    if form.validate_on_submit():
        # Check the email
        if User.query.filter_by(email=form.email.data).first():
            flash('Email already registered, Please use a different email address.', 'error-message')
        # Check the username
        if User.query.filter_by(name=form.name.data).first():
            flash('User already registered, Please use a different user.', 'error-message')

        # TODO Hash password before dropping to DB
        user = User(name=form.name.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Welcome {0} to the site, please sign in now.'.format(user.name))
        return redirect(url_for('home.index'))

    return render_template("auth/signup.html", form=form)


