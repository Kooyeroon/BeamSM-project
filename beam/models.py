# Importing necessary modules and functions
from beam import db, login_manager
from flask_login import UserMixin

# Function to load a user by their ID for flask-login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# User class representing users in the database
class User(db.Model, UserMixin):
    # Defining columns for the User table
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    # Relationship to LoadsBeam table, one-to-many relationship
    loads = db.relationship('LoadsBeam', backref='user', lazy=True)

    # String representation of User object
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

# LoadsBeam class representing loads on the beam in the database
class LoadsBeam(db.Model):
    # Defining columns for the LoadsBeam table
    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.Float, nullable=False)
    shear_force = db.Column(db.Float, nullable=False)
    bending_moment = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # String representation of LoadsBeam object
    def __repr__(self):
        return f"LoadsBeam('{self.position}', '{self.shear_force}', '{self.bending_moment}', '{self.user}')"
