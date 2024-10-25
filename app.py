from flask import Flask, redirect, url_for, render_template
from lab1 import lab1

app = Flask(__name__)
app.register_blueprint(lab1)

@app.route("/")
@app.route("/index")

def start():
    return redirect("/menu", code=302)

@app.route("/menu")
def menu():
     return """
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>

        <h1>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</h1>

        </header>
        <nav>
            <ul>
                <li><a href="/lab1">Первая лабораторная</a></li>
            </ul>
        </nav>
        <footer>
            &copy; Печенкин Владислав Витальевич, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
"""


flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']

@app.route('/lab2/flowers')
def list_flowers():
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Список всех цветов</h1>
    <p>Всего цветов: {len(flower_list)} </p>
    <p>Полный список: {flower_list} </p>
    </body>
</html>
'''


@app.route('/lab2/flowers/<int:flower_id>')
def show_flower(flower_id):
    if flower_id < 0 or flower_id >= len(flower_list):
        abort(404, 'цветок не найден')
    
    flower = flower_list[flower_id]
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Цветок</h1>
    <p>Название цветка: {flower} </p>
    <a href="/lab2/flowers">Вернуться к списку всех цветов</a>
    </body>
</html>
'''


@app.route('/lab2/clear_flowers')
def clear_flowers():
    global flower_list
    flower_list = []
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Список цветов очищен</h1>
    <a href="/lab2/flowers">Перейти к списку всех цветов</a>
    </body>
</html>
'''


@app.route('/lab2/add_flower/<name>')
def add_flower(name):
    flower_list.append(name)
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Добавлен новый цветок</h1>
    <p>Название нового цветка: {name} </p>
    <p>Всего цветов: {len(flower_list)}</p>
    <p>Полный список: {flower_list}</p>
    </body>
</html>
'''


@app.route('/lab2/example')
def example():
     name, lab_num, group, course = 'Владислав Печенкин', 2, 'ФБИ-24', 3
     fruits = [
        {'name': 'яблоко', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321},
    ]
     return render_template('example.html', 
                            name=name, lab_num=lab_num, group=group,
                            course=course, fruits=fruits)


@app.route('/lab2/')
def lab2():
     return render_template('lab2.html')


@app.route('/lab2/filters')
def filters():
     phrase = "0 <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
     return render_template('filter.html', phrase = phrase)