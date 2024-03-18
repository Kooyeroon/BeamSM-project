# Importing necessary modules and functions
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Creating Flask application instance
app = Flask(__name__)

# Secret key for session management
app.config['SECRET_KEY'] = '522006c50113414fb6ced20412eb5a4f'

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///beam.db'

# Initializing SQLAlchemy for database management
db = SQLAlchemy(app)

# Pushing application context
app.app_context().push()

# Initializing Bcrypt for password hashing
bcrypt = Bcrypt(app)

# Initializing LoginManager for user authentication
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# Importing routes after initializing app
from beam import routes
