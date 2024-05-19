from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField, SelectField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=8, message="Password must be at least 8 characters long."),
        Regexp(r'[A-Z]', message="Password must contain at least one uppercase letter."),
        Regexp(r'.*[0-9].*', message="Password must contain at least one number."),
        Regexp(r'.*[\!\@\#\$\%\^\&\*\(\)\-\_\=\+\[\]\{\}\;\:\'\"\,\<\.\>\?\/\|\\\`~].*', message="Password must contain at least one special character.")
    ])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(), EqualTo('password', message='Passwords must match')
    ])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')

class CreateRequestForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    file = FileField('Image')
    submit = SubmitField('Post')

class SortForm(FlaskForm):
    sorting_method = SelectField('Sort By', choices=[('newest', 'Newest'), ('oldest', 'Oldest')])
    submit = SubmitField('Sort')

class SearchForm(FlaskForm):
    search = StringField('Search', validators=[DataRequired()])
    submit = SubmitField('Search')

class CommentForm(FlaskForm):
    comment_content = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Post Comment')
