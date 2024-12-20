from flask import Blueprint, render_template, request, redirect, url_for, session
from db import db
from db.models import users, articles
from flask_login import login_user, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

lab8 = Blueprint('lab8', __name__)

@lab8.route('/lab8')
def index():
    username = session.get('username', 'anonymous')
    return render_template('lab8/lab8.html', username=username)

@lab8.route('/lab8/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('lab8/login.html')
    
    login_form = request.form.get('login')
    password_form = request.form.get('password')
    remember_me = request.form.get('remember_me') == 'on'

    if not login_form:
        return render_template('lab8/login.html', error='Логин не может быть пустым')
    if not password_form:
        return render_template('lab8/login.html', error='Пароль не может быть пустым')

    user = users.query.filter_by(login=login_form).first()

    if not user or not check_password_hash(user.password, password_form):
        return render_template('lab8/login.html', error='Ошибка входа: логин и/или пароль неверны')
    
    login_user(user, remember=remember_me)
    return redirect('/lab8/')

@lab8.route('/lab8/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab8/register.html')
    
    login_form = request.form.get('login')
    password_form = request.form.get('password')

    if not login_form:
        return render_template('lab8/register.html', error='Имя пользователя не может быть пустым')
    if not password_form:
        return render_template('lab8/register.html', error='Пароль не может быть пустым')
    
    login_exists = users.query.filter_by(login=login_form).first()
    if login_exists:
        return render_template('lab8/register.html', error='Такой пользователь уже существует')
    
    password_hash = generate_password_hash(password_form)
    new_user = users(login=login_form, password=password_hash)
    db.session.add(new_user)
    db.session.commit()

    login_user(new_user, remember=False)
    return redirect('/lab8/')

@lab8.route('/lab8/create', methods=['GET', 'POST'])
@login_required
def create_article():
    if request.method == 'GET':
        return render_template('lab8/create.html')
    
    title = request.form.get('title')
    content = request.form.get('content')

    if not title or not content:
        return render_template('lab8/create.html', error='Заголовок и содержимое не могут быть пустыми')
    
    new_article = articles(title=title, content=content, author=current_user)
    db.session.add(new_article)
    db.session.commit()
    return redirect(url_for('lab8.article_list'))

@lab8.route('/lab8/edit/<int:article_id>', methods=['GET', 'POST'])
@login_required
def edit_article(article_id):
    article = articles.query.get_or_404(article_id)

    if article.author != current_user:
        return "У вас нет прав на редактирование этой статьи", 403

    if request.method == 'GET':
        return render_template('lab8/edit.html', article=article)
    
    article.title = request.form.get('title')
    article.content = request.form.get('content')
    db.session.commit()
    return redirect(url_for('lab8.article_list'))

@lab8.route('/lab8/delete/<int:article_id>', methods=['POST'])
@login_required
def delete_article(article_id):
    article = articles.query.get_or_404(article_id)

    if article.author != current_user:
        return "У вас нет прав на удаление этой статьи", 403

    db.session.delete(article)
    db.session.commit()
    return redirect(url_for('lab8.article_list'))
    
@lab8.route('/lab8/articles/')
@login_required
def article_list():
    articles_list = articles.query.filter_by(author=current_user).all()
    return render_template('lab8/articles.html', articles=articles_list)

@lab8.route('/lab8/logout/')
@login_required
def logout():
    logout_user()
    return redirect('/lab8/')

@lab8.route('/lab8/public_articles/')
def public_articles():
    public_articles = articles.query.filter_by(is_public=True).all()
    return render_template('lab8/public_articles.html', articles=public_articles)

@lab8.route('/lab8/search', methods=['GET', 'POST'])
def search_articles():
    if request.method == 'GET':
        return render_template('lab8/search.html')
    
    query = request.form.get('query')
    if not query:
        return render_template('lab8/search.html', error='Пожалуйста, введите запрос для поиска')
    
    if current_user.is_authenticated:
        user_articles = articles.query.filter(
            (articles.author == current_user) | (articles.is_public == True)
        ).filter(
            (articles.title.contains(query)) | (articles.content.contains(query))
        ).all()
    else:
        user_articles = articles.query.filter_by(is_public=True).filter(
            (articles.title.contains(query)) | (articles.content.contains(query))
        ).all()
    
    return render_template('lab8/search_results.html', articles=user_articles, query=query)