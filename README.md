# flask_app_boiler
Flask boilerplate app

The purpose of this repo is to build a simple boilerplate for my apps to deploy web ideas quickly.

# Features
- Flask Setup for expansion via MVC
    + Default site pages controlled with Flask Blueprints [app/home folder]
    + Authentication built in [app/auth folder].
    + DB controlled by SQLAlchemy [SQLite by default]

- Bootstrap Themes via Bootswatch CDN
	+ Just change out the link in `app/templates/base.html`
	+ https://www.bootstrapcdn.com/bootswatch/


# Install
_I wrote it for Python 3.6, but it may work in Python 2.7 YMMV_

- `git clone https://github.com/spdz/flask_app_boiler.git`
- `cd flask_app_boiler`
- `pip install requirements.txt`
- `virtualenv -p python3 .`
- `export FLASK_APP=run.py`
- `export FLASK_CONFIG=development`
- `flask run`

Open `http://127.0.0.1:5000/` in browser of choice. 


### DB Operations for firt time use

- Init the DB
- `flask db init`
- Perform Migrations
- `flask db migrate`
- DB Upgrades
- `flask db upgrade`


Originally uploaded to my github repo:
https://github.com/spdz/flask_app_boiler

