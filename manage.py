# manage.py


import os
# import unittest
# import coverage

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from run import app
from app import db
from app.auth.models import User

migrate = Migrate(app, db)
manager = Manager(app)

# migrations
manager.add_command('db', MigrateCommand)

# # TODO implement tests
# @manager.command
# def test():
#     """Runs the unit tests without coverage."""
#     tests = unittest.TestLoader().discover('tests')
#     result = unittest.TextTestRunner(verbosity=2).run(tests)
#     if result.wasSuccessful():
#         return 0
#     else:
#         return 1

# # TODO implement coverage
# @manager.command
# def cov():
#     """Runs the unit tests with coverage."""
#     cov = coverage.coverage(branch=True, include='project/*')
#     cov.start()
#     tests = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=2).run(tests)
#     cov.stop()
#     cov.save()
#     print('Coverage Summary:')
#     cov.report()
#     basedir = os.path.abspath(os.path.dirname(__file__))
#     covdir = os.path.join(basedir, 'tmp/coverage')
#     cov.html_report(directory=covdir)
#     print('HTML version: file://%s/index.html' % covdir)
#     cov.erase()


@manager.command
def create_db():
    """Creates the db tables."""
    db.create_all()


@manager.command
def drop_db():
    """Drops the db tables."""
    db.drop_all()


@manager.command
def create_admin():
    """Creates the admin user."""
    user = User(email="admin@example.com",
                    name="admin",
                    password="hunter2")

    user.is_admin = True

    db.session.add(user)
    db.session.commit()


if __name__ == '__main__':
    manager.run()