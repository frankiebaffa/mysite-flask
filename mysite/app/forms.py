from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class ArticleCreateForm(FlaskForm):
    body = StringField('Body', validators=[DataRequired()])
    url = StringField('URL', validators=[DataRequired()])
    imageurl = StringField('Image File Name', validators=[DataRequired()])
    submit = SubmitField('Post')

class PostCreateForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    body = StringField('Body', validators=[DataRequired()])
    imageurl = StringField('Image File Name', validators=[DataRequired()])
    submit = SubmitField('Post')

class ProjectCreateForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    body = StringField('Body', validators=[DataRequired()])
    url = StringField('URL', validators=[DataRequired()])
    imageurl = StringField('Image File Name', validators=[DataRequired()])
    submit = SubmitField('Post')
