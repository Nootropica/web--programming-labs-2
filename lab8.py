from flask import Blueprint, render_template, request, redirect, url_for, session


lab8 = Blueprint('lab8', __name__)

@lab8.route('/lab8')
def index():
    username = session.get('username', 'anonymous')
    return render_template('lab8/lab8.html', username=username)

@lab8.route('/lab8/login', methods=['GET', 'POST'])
def login():
        return render_template('lab/login.html')

@lab8.route('/lab8/register', methods=['GET', 'POST'])
def register():
        return render_template('lab8/register.html')

@lab8.route('/lab8/create', methods=['GET', 'POST'])
def create():
        return render_template('lab8/create.html')
    
@lab8.route('/lab8/articles', methods=['GET', 'POST'])
def articles():
        return render_template('lab8/articles.html')
