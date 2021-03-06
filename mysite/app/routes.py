from app import app, db, models
from app.models import Article, User, Post, Project, About
from os import walk
from flask import Flask, url_for, render_template, redirect, flash, request
from flask_login import current_user, login_user, logout_user
from app.forms import LoginForm, ArticleCreateForm, PostCreateForm
from app.forms import ProjectCreateForm, ContactForm, PostEditForm
from app.forms import ArticleEditForm, ProjectEditForm, AboutCreateForm
from app.forms import AboutEditForm
from werkzeug.urls import url_parse
import sqlite3
from flask_nav import Nav
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_mail import Message, Mail

mail = Mail()
photos = UploadSet('photos', IMAGES)

# Route to home page should be root, index, and the recent projects directory
@app.route('/')
@app.route('/index')
@app.route('/index/')
def index():
    allprojects = Project.query.order_by(Project.timestamp.desc()).all()
    allarticles = Article.query.order_by(Article.timestamp.desc()).all()
    allposts = Post.query.order_by(Post.timestamp.desc()).all()
    aboutparagraphs = About.query.order_by(About.id).all()
    return render_template('indexscroll.html', allprojects=allprojects,
        allposts=allposts, allarticles=allarticles, aboutparagraphs=aboutparagraphs)

#@app.route('/projects')
#@app.route('/projects/')
#def projects():
    # Query all projects with timestamp descending
#    results = Project.query.order_by(Project.timestamp.desc()).all()
#    return render_template('projects.html', allprojects=results)

#@app.route('/articles')
#@app.route('/articles/')
#def articles():
    # Query all articles by timestamp descending
#    results = Article.query.order_by(Article.timestamp.desc()).all()
#    return render_template('articles.html', allarticles=results)

#@app.route('/blog', methods=['GET', 'POST'])
#@app.route('/blog/', methods=['GET', 'POST'])
#def blog():
    # Query all Posts by timestamp descending
#    results = Post.query.order_by(Post.timestamp.desc()).all()
#    return render_template('blog.html', allposts=results)

@app.route('/blog/<id>', methods=['GET', 'POST'])
@app.route('/blog/<id>/', methods=['GET', 'POST'])
def blogpost(id):
    # Query single post by returned id
    post = Post.query.get(id)
    return render_template('blogpost.html', post=post)

@app.route('/projects/<id>', methods=['GET', 'POST'])
@app.route('/projects/<id>/', methods=['GET', 'POST'])
def projectitem(id):
    project = Project.query.get(id)
    return render_template('projectitem.html', projectitem=project)

@app.route('/login', methods=['GET', 'POST'])
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('manage'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('manage')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/contact', methods=['GET', 'POST'])
@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    aboutparagraphs = About.query.order_by(About.id).all()
    sent = ''
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form, aboutparagraphs=aboutparagraphs)
        else:
            msg = Message(form.subject.data, sender='frankiebaffa.com@gmail.com',
                recipients=['frankiebaffa@gmail.com'])
            msg.body = """
            From: %s <%s>

            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            sent = 'Your message has been sent!'
            return render_template('contact.html', form=form, sent=sent, aboutparagraphs=aboutparagraphs)

    elif request.method == 'GET':
        return render_template('contact.html', form=form, sent=sent, aboutparagraphs=aboutparagraphs)

@app.route('/aboutm')
@app.route('/aboutme/')
def aboutme():
    about = About.query.order_by(About.id).first()
    return render_template('aboutme.html', about=about)

#==============================================================================
#   External redirects
#==============================================================================

@app.route('/nominal')
@app.route('/nominal/')
def nominal():
    return redirect('https://soundcloud.com/iamnominal')

@app.route('/dds')
@app.route('/dds/')
def dds():
    return redirect('https://soundcloud.com/doobiedecibelsystem')

@app.route('/podcast')
@app.route('/podcast/')
def podcast():
    return redirect('http://soundcloud.com/letsbefrankpodcast')

#==============================================================================
#   All routes beneath must have user authenticated
#==============================================================================

@app.route('/manage')
@app.route('/manage/')
def manage():
    if current_user.is_authenticated:
        results = User.query.order_by(User.id.asc()).all()
        return render_template('manage.html', items=results)
    else:
        return redirect(url_for('index'))

# Route to upload page to add pictures to blog, article, and project posts.
# I am figuring out how to implement flask-upload into the forms existing on
# the manage/model pages so that the imageurl will not need to be typed in and
# will automatically be included in the object with a submission of the form.
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        imageurl = request.form.get("imageurl")
        photos.save(request.files['photo'], name=imageurl + '.')
        return redirect(url_for('manage'))
    return render_template('upload.html')

@app.route('/manage/about', methods=['GET', 'POST'])
@app.route('/manage/about/', methods=['GET', 'POST'])
def manageabout():
    if current_user.is_authenticated:
        createform = AboutCreateForm()
        results = About.query.order_by(About.id).all()
        editform = AboutEditForm()

        return render_template('manageabout.html', title='Manage About',
            createform=createform, editform=editform, items = results)
 
        if createform.validate_on_submit():
            about = About(body=createform.body.data, author=current_user)
            db.session.add(about)
            db.session.commit()
            flash('Posted')
            return redirect(url_for('manageabout'))
    else:
        return redirect(url_for('index'))

@app.route('/manage/articles', methods=['GET', 'POST'])
@app.route('/manage/articles/', methods=['GET', 'POST'])
def managearticles():
    if current_user.is_authenticated:
        createform = ArticleCreateForm()
        editform = ArticleEditForm()
        
        createform.imagefile = imageselect(createform.imagefile)
        editform.imagefile = imageselect(editform.imagefile)

        if createform.validate_on_submit():
            article = Article(body=createform.body.data,
                url=createform.url.data,
                imageurl=createform.imagefile.data,
                author=current_user)
            db.session.add(article)
            db.session.commit()
            flash('Posted!')
            return redirect(url_for('managearticles'))
        results = Article.query.order_by(Article.timestamp.desc()).all()
        return render_template('managearticles.html', title='Manage Articles',
            createform=createform, editform=editform, items=results)
    else:
        return redirect(url_for('index'))

@app.route('/manage/posts', methods=['GET', 'POST'])
@app.route('/manage/posts/', methods=['GET', 'POST'])
def manageposts():
    if current_user.is_authenticated:
        createform = PostCreateForm()
        editform = PostEditForm()

        createform.imagefile = imageselect(createform.imagefile)
        editform.imagefile = imageselect(editform.imagefile)

        if createform.validate_on_submit():
            post = Post(title=createform.title.data, body=createform.body.data,
                imageurl=createform.imagefile.data,
                author=current_user)
            db.session.add(post)
            db.session.commit()
            flash('Posted!')
            return redirect(url_for('manageposts'))

        results = Post.query.order_by(Post.timestamp.desc()).all()
        return render_template('manageposts.html', title='Manage Posts',
            createform=createform, editform=editform, items=results)
    else:
        return redirect(url_for('index'))

@app.route('/manage/projects', methods=['GET', 'POST'])
@app.route('/manage/projects/', methods=['GET', 'POST'])
def manageprojects():
    if current_user.is_authenticated:
        createform = ProjectCreateForm()
        editform = ProjectEditForm()

        createform.imagefile = imageselect(createform.imagefile)
        editform.imagefile = imageselect(editform.imagefile)

        if createform.validate_on_submit():
            project = Project(title=createform.title.data, body=createform.body.data,
                url=createform.url.data,
                imageurl=url_for('static', filename='img/{}'.format(createform.imagefile.data)),
                author=current_user)
            db.session.add(project)
            db.session.commit()
            flash('Posted')
            return redirect(url_for('manageprojects'))
        results = Project.query.order_by(Project.timestamp.desc()).all()
        return render_template('manageprojects.html', title='Manage Projects',
            createform=createform, editform=editform, items=results)

@app.route('/manage/articles/delete', methods=['POST'])
def deletearticle():
    if current_user.is_authenticated:
        body = request.form.get("body")
        article = Article.query.filter_by(body=body).first()
        db.session.delete(article)
        db.session.commit()
        return redirect(url_for('managearticles'))
    else:
        return redirect(url_for('index'))

@app.route('/manage/about/delete', methods=['POST'])
def deleteabout():
    if current_user.is_authenticated:
        id = request.form.get("id")
        about = About.query.filter_by(id=id).first()
        db.session.delete(about)
        db.session.commit()
        return redirect(url_for('manageabout'))
    else:
        return redirect(url_for('index'))

@app.route('/manage/posts/delete', methods=['POST'])
def deletepost():
    if current_user.is_authenticated:
        title = request.form.get("title")
        post = Post.query.filter_by(title=title).first()
        db.session.delete(post)
        db.session.commit()
        return redirect(url_for('manageposts'))
    else:
        return redirect(url_for('index'))

@app.route('/manage/projects/delete', methods=['POST'])
def deleteproject():
    if current_user.is_authenticated:
        title = request.form.get("title")
        project = Project.query.filter_by(title=title).first()
        db.session.delete(project)
        db.session.commit()
        return redirect("/manage/projects")
    else:
        return redirect(url_for('index'))

@app.route('/manage/articles/update', methods=['POST'])
def updatearticle():
    if current_user.is_authenticated:
        newbody = request.form.get("newbody")
        oldbody = request.form.get("oldbody")
        newurl = request.form.get("newurl")
        imagefile = request.form.get("imagefile")
        newimageurl = request.form.get("newimageurl")
        article = Article.query.filter_by(body=oldbody).first()
        article.body = newbody
        article.url = newurl
        article.imageurl = imagefile
        db.session.commit()
        return redirect(url_for('managearticles'))
    else:
        return redirect(url_for('index'))

@app.route('/manage/about/update', methods=['POST'])
def updateabout():
    if current_user.is_authenticated:
        newbody = request.form.get("newbody")
        id = request.form.get("id")
        about = About.query.filter_by(id=id).first()
        about.body = newbody
        db.session.commit()
        return redirect(url_for('manageabout'))
    else:
        return redirect(url_for('index'))

@app.route('/manage/posts/update', methods=['POST'])
def updatepost():
    if current_user.is_authenticated:
        newtitle = request.form.get("newtitle")
        oldtitle = request.form.get("oldtitle")
        newbody = request.form.get("newbody")
        imagefile = request.form.get("imagefile")
        newimageurl = request.form.get("newimageurl")
        post = Post.query.filter_by(title=oldtitle).first()
        post.title = newtitle
        post.body = newbody
        post.imageurl = imagefile
        db.session.commit()
        return redirect(url_for('manageposts'))
    else:
        return redirect(url_for('index'))

@app.route('/manage/projects/update', methods=['POST'])
def updateproject():
    if current_user.is_authenticated:
        newtitle = request.form.get("newtitle")
        oldtitle = request.form.get("oldtitle")
        newbody = request.form.get("newbody")
        newurl = request.form.get("newurl")
        imagefile = request.form.get("imagefile")
        project = Project.query.filter_by(title=oldtitle).first()
        project.title = newtitle
        project.body = newbody
        project.url = newurl
        project.imageurl = imagefile
        db.session.commit()
        return redirect(url_for('manageprojects'))
    else:
        return redirect(url_for('index'))

@app.route('/logout')
@app.route('/logout/')
def logout():
    if current_user.is_authenticated:
        logout_user()
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

#==============================================================================
#   Error Pages
#==============================================================================

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

#==============================================================================
#   Functions
#==============================================================================

def imageselect(selectfield):
    imagefiles = []
    for (dirpath, dirnames, filenames) in walk(app.config['UPLOADED_PHOTOS_DEST']):
        for i in range(len(filenames)):
            imagefiles.append(filenames[i])
    selectfield.choices = [(url_for('static', filename='img/uploads/{}'.format(imagefiles[i])), imagefiles[i]) for i in range(len(imagefiles))]
    return selectfield
