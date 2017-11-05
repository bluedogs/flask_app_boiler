# Basic Flask imports
from flask import Blueprint, request, render_template, \
                    flash, g, session, redirect, url_for
from werkzeug import check_password_hash
from passlib.hash import sha256_crypt

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

            if user and sha256_crypt.verify(user.password, request.form['password']):
                session['logged_in'] = True
                session['username'] = request.form['email']
                flash('You are now logged in', 'success')
                return redirect(url_for('home.index'))
            else:
                error = 'Invalid login'
                return render_template('auth/signin.html', error=error, form=form)
            flash('Wrong email or password', 'error-message')
            error = 'Something went wrong.'
            return render_template("auth/signin.html", error=error, form=form)
    return render_template("auth/signin.html", form=form)


@mod_auth.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        password = sha256_crypt.encrypt(str(form.password.data))
        print(name, email, password)
        # Check the email
        if User.query.filter_by(email=form.email.data).first():
            flash('Email already registered, Please use a different email address.', 'error-message')
        # Check the username
        if User.query.filter_by(name=form.name.data).first():
            flash('User already registered, Please use a different user.', 'error-message')

        user = User(name, email, password)
        print("Added user {0}".format(user.name))
        db.session.add(user)
        db.session.commit()
        flash('Welcome {0} to the site, please sign in now.'.format(name))
        return redirect(url_for('.signin'))

    return render_template("auth/signup.html", form=form)


