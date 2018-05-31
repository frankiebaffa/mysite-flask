from app import app, db, models
from app.models import Article, User
from flask import Flask, render_template, redirect, flash, request
from flask_login import current_user, login_user, logout_user
from app.forms import LoginForm, ArticleCreateForm
from werkzeug.urls import url_parse
import sqlite3

def connect_db():
    return sqlite3.connect('app.db')

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/articles')
def articles():
    database = connect_db()
    cur = database.execute('select body, url, imageurl, timestamp from Article ' +
        'order by timestamp desc')
    columns = [column[0] for column in cur.description]
    results = []
    for row in cur.fetchall():
        results.append(dict(zip(columns, row)))
    return render_template('articles.html', allarticles=results)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/manage')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect('/login')
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = '/manage'
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/manage')
def manage():
    if current_user.is_authenticated:
        return render_template('manage.html')
    else:
        return redirect('/index')

@app.route('/manage/articles', methods=['GET', 'POST'])
def managearticles():
    if current_user.is_authenticated:
        createform = ArticleCreateForm()
        if createform.validate_on_submit():
            article = Article(body=createform.body.data, url=createform.url.data,
                imageurl=createform.imageurl.data, author=current_user)
            db.session.add(article)
            db.session.commit()
            flash('Posted!')
            return redirect('/manage/articles')
        database = connect_db()
        cur = database.execute('select id, body, timestamp, url, imageurl ' +
        'from Article order by timestamp desc')
        columns = [column[0] for column in cur.description]
        results = []
        for row in cur.fetchall():
            results.append(dict(zip(columns, row)))
        return render_template('managearticles.html', title='Manage Articles',
            createform=createform, items=results)
    else:
        return redirect('/index')

@app.route('/manage/articles/edit', methods=['GET', 'POST'])
def editarticle():
    if current_user.is_authenticated:
        editform = ArticleEditForm()
        if editform.validate_on_submit():
            body = request.form.get("body")
            article = Article.query.filter_by(body=body).first()
            #if editform.body.data != "":
            article.body = editform.body.data
            if editform.url.data != "":
                article.url = editform.url.data
            if editform.imageurl.data != "":
                article.imageurl = editform.imageurl.data
            db.session.commit()
            return redirect('/manage/articles')
        database = connect_db()
        cur = database.execute('select id, body, timestamp, url, imageurl ' +
        'from Article order by timestamp desc')
        columns = [column[0] for column in cur.description]
        results = []
        for row in cur.fetchall():
            results.append(dict(zip(columns, row)))
        return render_template('editarticles.html', title='Manage Articles',
            editform=editform)
@app.route('/manage/articles/delete', methods=['POST'])
def deletearticle():
    if current_user.is_authenticated:
        body = request.form.get("body")
        article = Article.query.filter_by(body=body).first()
        db.session.delete(article)
        db.session.commit()
        return redirect("/manage/articles")
    else:
        return redirect("/index")

@app.route('/manage/articles/update', methods=['POST'])
def updatearticle():
    if current_user.is_authenticated:
        newbody = request.form.get("newbody")
        oldbody = request.form.get("oldbody")
        newurl = request.form.get("newurl")
        newimageurl = request.form.get("newimageurl")
        article = Article.query.filter_by(body=oldbody).first()
        article.body = newbody
        article.url = newurl
        article.imageurl = newimageurl
        db.session.commit()
        return redirect("/manage/articles")
    else:
        return redirect("/index")

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')

@app.route('/nominal')
def nominal():
    return redirect('https://soundcloud.com/iamnominal')

@app.route('/dds')
def dds():
    return redirect('https://soundcloud.com/doobiedecibelsystem')

@app.route('/podcast')
def podcast():
    return redirect('http://soundcloud.com/letsbefrankpodcast')

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/index')
