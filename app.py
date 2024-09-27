from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/index")

def start():
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

@app.route("/lab1")
def lab1():
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
        
        <footer>
            &copy; Владислав Печенкин, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
"""
