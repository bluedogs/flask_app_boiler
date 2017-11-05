from app import db

class Base(db.Model):
    """ Base table template """

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


#
# User model
#
class User(Base):
    """ User Object and Table Model """

    __tablename__ = 'auth_user'

    # Basics
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(192), nullable=False)
    # # Roles
    # role = db.Column(db.SmallInteger, nullable=False)
    # status = db.Column(db.SmallInteger, nullable=False)

    # New user init
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    # Return function
    def __repr__(self):
        return '<User {}>'.format(self.name)

