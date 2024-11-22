from flask import Blueprint, render_template, session

lab5 = Blueprint('lab5', __name__)

@lab5.route('/lab5')
def index():
    username = session.get('username', 'anonymous')
    return render_template('lab5/menu.html', username=username)

@lab5.route('/lab5/login')
def login():
    return "Страница входа"

@lab5.route('/lab5/register')
def register():
    return "Страница регистрации"

@lab5.route('/lab5/list')
def list_articles():
    return "Список статей"

@lab5.route('/lab5/create')
def create_article():
    return "Создание статьи"