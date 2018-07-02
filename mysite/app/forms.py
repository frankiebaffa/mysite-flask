from os import walk
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import TextAreaField, SelectField, validators
from wtforms.validators import DataRequired

# Create form for logging-in users
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={"placeholder": " Username"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": " Password"})
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

# Create form for creating a new article
class ArticleCreateForm(FlaskForm):
    body = StringField('Body', validators=[DataRequired()], render_kw={"placeholder": " Title"})
    url = StringField('URL', validators=[DataRequired()], render_kw={"placeholder": " URL"})
    imagefile = SelectField('Image', choices=[('x', 'x')], coerce=str)
    submit = SubmitField('Post')

# Create form for creating new blog post
class PostCreateForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()], render_kw={"placeholder": " Title"})
    imagefile = SelectField('Image', choices=[('x', 'x')], coerce=str)
    body = TextAreaField('Body', validators=[DataRequired()], render_kw={"placeholder": " Body"})
    submit = SubmitField('Post')

# Create form for creating new recent project
class ProjectCreateForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()], render_kw={"placeholder": " Title"})
    url = StringField('URL', validators=[DataRequired()], render_kw={"placeholder": " URL"})
    imagefile = SelectField('Image', choices=[('x', 'x')], coerce=str)
    body = TextAreaField('Body', validators=[DataRequired()], render_kw={"placeholder": " Body"})
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
    newbody = StringField('Body', validators=[DataRequired()], render_kw={"placeholder": " Title"})
    newurl = StringField('URL', validators=[DataRequired()], render_kw={"placeholder": " URL"})
    newimageurl = StringField('Image File Name', validators=[DataRequired()], render_kw={"placeholder": " Image URL"})
    submit = SubmitField('Update')

class PostEditForm(FlaskForm):
    newtitle = StringField('Title', validators=[DataRequired()], render_kw={"placeholder": " Title"})
    imagefile = SelectField('Image', choices=[('x', 'x')], coerce=str)
    newimageurl = StringField('Image File Name', validators=[DataRequired()], render_kw={"placeholder": " Image URL"})
    newbody = TextAreaField('Body', validators=[DataRequired()], render_kw={"placeholder": " Body"})
    submit = SubmitField('Update')

class ProjectEditForm(FlaskForm):
    newtitle = StringField('Title', validators=[DataRequired()], render_kw={"placeholder": " Title"})
    newurl = StringField('URL', validators=[DataRequired()], render_kw={"placeholder": " URL"})
    newimageurl = StringField('Image File Name', validators=[DataRequired()], render_kw={"placeholder": " Image URL"})
    newbody = TextAreaField('Body', validators=[DataRequired()], render_kw={"placeholder": " Body"})
    submit = SubmitField('Update')

class AboutCreateForm(FlaskForm):
    body = TextAreaField('Body', validators=[DataRequired()], render_kw={"placeholder": " Body Paragraph"})
    submit = SubmitField('Create')

class AboutEditForm(FlaskForm):
    newbody = TextAreaField('Body', validators=[DataRequired()], render_kw={"placeholder": " Body Paragraph"})
    submit = SubmitField('Update')
