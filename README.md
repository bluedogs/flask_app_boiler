# flask_api_boiler
Flask API boilerplate [Flask, Vue, RethinkDB]

Using the following as a starting point:
https://www.pluralsight.com/guides/python/build-a-simple-file-storage-service-using-vuejs-flask-and-rethinkdb

The purpose of this repo is to build a simple boilerplate for my apps to deploy web ideas quickly. I love Python and Flask, and am learning Vue.js and RethinkDB.

# Features
- Flask backend for API endpoints
    + Authentication endpoints and API tokens built in.
    + Just need to add custom routes for the next app.
- RethinkDB for DB operations
    + Basic DB scheme with users
- Vue.js for the front end
    + Basic theme with minimalism in mind.

# Install
_I wrote it for Python 3.6, but it may work in Python 2.7 YMMV_

- `git clone https://github.com/spdz/flask_api_boiler.git`
- `cd flask_api_boiler`
- `pip install requirements.txt`
- `python app.py`

Open `http://127.0.0.1:5000/` in browser of choice. 