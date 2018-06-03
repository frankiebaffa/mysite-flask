from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

# Create form for logging-in users
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

# Create form for creating a new article
class ArticleCreateForm(FlaskForm):
    body = StringField('Body', validators=[DataRequired()])
    url = StringField('URL', validators=[DataRequired()])
    imageurl = StringField('Image File Name', validators=[DataRequired()])
    submit = SubmitField('Post')

# Create form for creating new blog post
class PostCreateForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    body = StringField('Body', validators=[DataRequired()])
    imageurl = StringField('Image File Name', validators=[DataRequired()])
    submit = SubmitField('Post')

# Create form for creating new recent project
class ProjectCreateForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    body = StringField('Body', validators=[DataRequired()])
    url = StringField('URL', validators=[DataRequired()])
    imageurl = StringField('Image File Name', validators=[DataRequired()])
    submit = SubmitField('Post')
