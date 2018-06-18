from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import TextAreaField, validators
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
    imageurl = StringField('Image File Name', validators=[DataRequired()])
    body = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField('Post')

# Create form for creating new recent project
class ProjectCreateForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    url = StringField('URL', validators=[DataRequired()])
    imageurl = StringField('Image File Name', validators=[DataRequired()])
    body = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField('Post')

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()], render_kw={"placeholder": " Name"})
    email = StringField('Email Address', [validators.Required(), validators.Email()],
        render_kw={"placeholder": " Email"})
    subject = StringField('Subject', validators=[DataRequired()],
        render_kw={"placeholder": " Subject"})
    message = TextAreaField("Message", validators=[DataRequired()],
        render_kw={"placeholder": " Message"})
    submit = SubmitField('Send')

class ArticleEditForm(FlaskForm):
    newbody = StringField('Body', validators=[DataRequired()])
    newurl = StringField('URL', validators=[DataRequired()])
    newimageurl = StringField('Image File Name', validators=[DataRequired()])
    submit = SubmitField('Update')

class PostEditForm(FlaskForm):
    newtitle = StringField('Title', validators=[DataRequired()])
    newimageurl = StringField('Image File Name', validators=[DataRequired()])
    newbody = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField('Update')

class ProjectEditForm(FlaskForm):
    newtitle = StringField('Title', validators=[DataRequired()])
    newurl = StringField('URL', validators=[DataRequired()])
    newimageurl = StringField('Image File Name', validators=[DataRequired()])
    newbody = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField('Update')

class AboutCreateForm(FlaskForm):
    body = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField('Create')

class AboutEditForm(FlaskForm):
    newbody = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField('Update')
