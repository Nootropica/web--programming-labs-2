from flask import Flask
app = Flask(__name__)

@app.route("/")
def start():
    return """
<!doctype html>
<html>
    <head>
        <title>Печенкин Владислав Витальевич, лабораторная 1</title>
    </head>
    <body>
        <header>

        <h1>web-сервер на flask</h1>

        <footer>
            &copy; Владислав Печенкин, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
"""