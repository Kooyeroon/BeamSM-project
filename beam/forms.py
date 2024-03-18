# Importing necessary modules and functions
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from beam.models import User

# Form for user registration
class RegistrationForm(FlaskForm):
    # Username field with validation
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    # Email field with validation
    email = StringField('Email', validators=[DataRequired(), Email()])
    # Password field with validation
    password = PasswordField('Password', validators=[DataRequired()])
    # Confirm password field with validation
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    # Submit button
    submit = SubmitField('Sign Up')

    # Custom validation to check if the username already exists
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    # Custom validation to check if the email already exists
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

# Form for user login
class LoginForm(FlaskForm):
    # Email field with validation
    email = StringField('Email', validators=[DataRequired(), Email()])
    # Password field with validation
    password = PasswordField('Password', validators=[DataRequired()])
    # Checkbox to remember user session
    remember = BooleanField('Remember Me')
    # Submit button
    submit = SubmitField('Login')

