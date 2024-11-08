from flask import Blueprint, redirect, url_for
lab1 = Blueprint('lab1', __name__)


def start():
    return redirect("/menu", code=302)


@lab1.route("/menu")
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
                <li><a href="/lab2">Вторая лабораторная</a></li>
                <li><a href="/lab3">Третья лабораторная</a></li>
                <li><a href="/lab4">Четвертая лабораторная</a></li>
            </ul>
        </nav>
        <footer>
            &copy; Печенкин Владислав Витальевич, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
"""


@lab1.route("/lab1/")
def lab():
     return """
<!doctype html>
<html>
    <head>
        <title>Печенкин Владислав Витальевич, лабораторная 1</title>
    </head>
    <body>
        <header>

        <h1>web-сервер на flask</h1>

        </header>

        <p>
        Flask — фреймворк для создания веб-приложений на языке
        программирования Python, использующий набор инструментов
        Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
        называемых микрофреймворков — минималистичных каркасов веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        </p>

        <nav>
            <ul>
                <li><a href="/menu">Меню</a></li>
            </ul>
        </nav>

        <h2>Реализованные роуты</h2>

        <nav>
            <ul>
                <li><a href="/lab1/oak">Дуб</a></li>
                <li><a href="/lab1/student">Студент</a></li>
                <li><a href="/lab1/python">Python</a></li>
                <li><a href="/lab1/personal">Personal</a></li>
            </ul>
        </nav>

        <footer>
            &copy; Владислав Печенкин, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
"""


@lab1.route('/lab1/oak')
def oak():
     return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='/lab1/lab1.css') + '''">
        <title>Дуб</title>
    </head>
    <body>
        <h1>Дуб</h1>
        <img src="''' + url_for('static', filename='/lab1/oak.jpg') + '''">
    </body>
</html>
'''


@lab1.route('/lab1/student')
def student():
     return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='/lab1/lab1.css') + '''">
        <title>Студент</title>
    </head>
    <body>
        <h1>Печенкин Владислав Витальевич</h1>
        <img src="''' + url_for('static', filename='/lab1/logo.png') + '''" class="Student">
    </body>
</html>
'''


@lab1.route('/lab1/python')
def python():
     return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='/lab1/lab1.css') + '''">
        <title>Python</title>
    </head>
    <body>
        <h1>Что такое Python?</h1>
        <p>
            Python — это скриптовый язык программирования. Он универсален, поэтому 
            подходит для решения разнообразных задач и для многих платформ: начиная 
            с iOS и Android и заканчивая серверными операционными системами.
        </p>
        <p>
            Это интерпретируемый язык, а не компилируемый, как C++ или Java. 
            Программа на Python представляет собой обычный текстовый файл. 
            Код можно писать практически в любом редакторе или использовать 
            специальные IDE:
        </p>
        <img src="''' + url_for('static', filename='/lab1/python.png') + '''"class="Python">
    </body>
</html>
'''


@lab1.route('/lab1/personal')
def personal():
     return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='/lab1/lab1.css') + '''">
        <title>Hyundai Solaris</title>
    </head>
    <body>
                <h1>Hyundai Solaris</h1>
        <p>
            Hyundai Solaris 2011 года выпуска — это бюджетный седан, который стал 
            одной из самых популярных моделей на российском рынке благодаря сочетанию 
            доступной цены, надежности и функциональности. Разработанный на базе Hyundai 
            Accent, Solaris был адаптирован специально для российских условий эксплуатации, 
            что позволило ему завоевать доверие среди автолюбителей. Машина оснащена 
            современным дизайном, плавными линиями кузова и аккуратными фарами, что 
            придает ей динамичный и привлекательный внешний вид.
        </p>
        <p>
            Под капотом Hyundai Solaris 2011 года можно найти бензиновые двигатели 
            объемом 1,4 или 1,6 литра, которые обеспечивают неплохую динамику для 
            городских условий. Машина предлагается как с механической, так и с 
            автоматической коробкой передач, что позволяет водителю выбрать вариант 
            под свои предпочтения. Благодаря продуманной подвеске, Solaris демонстрирует 
            хорошую управляемость и комфортное движение по не всегда идеальным дорогам.
        </p>
        <p>
        Внутри автомобиля можно отметить эргономичный салон с удобным 
        расположением органов управления и достаточно просторное внутреннее 
        пространство для автомобиля такого класса. Несмотря на бюджетность модели, 
        в ней можно найти полезные опции, такие как кондиционер, подогрев сидений 
        и мультимедийную систему. Hyundai Solaris 2011 года выпуска зарекомендовал 
        себя как практичный и экономичный автомобиль для повседневных поездок в городских условиях.
        </p>
        <img src="''' + url_for('static', filename='/lab1/car.jpg') + '''"class="Car">
    </body>
</html>
'''