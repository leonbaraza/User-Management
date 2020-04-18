from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email


class EmailPasswordForm(FlaskForm):
    email = StringField('Email Address', validators=[DataRequired('Please enter your email address'), Email('Check if the email address you entered is valid')])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
