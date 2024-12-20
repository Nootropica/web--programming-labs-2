from flask import Blueprint, render_template, request, redirect, session

lab4 = Blueprint('lab4', __name__)

@lab4.route('/lab4/')
def lab():
    return render_template('lab4/lab4.html')

@lab4.route('/lab4/div-form')
def div_form():
    return render_template('lab4/div-form.html')

@lab4.route('/lab4/div', methods=['POST'])
def div():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    
    if x1 == '' or x2 == '':
        return render_template('lab4/div.html', error='Оба поля должны быть заполнены!')
    
    x1 = int(x1)
    x2 = int(x2)
    
    if x2 == 0:
        return render_template('lab4/div.html', error='На ноль делить нельзя!')
    
    result = x1 / x2
    return render_template('lab4/div.html', x1=x1, x2=x2, result=result)

@lab4.route('/lab4/sum-form')
def sum_form():
    return render_template('lab4/sum-form.html')

@lab4.route('/lab4/sum', methods=['POST'])
def sum():
    x1 = request.form.get('x1', '')
    x2 = request.form.get('x2', '')
    
    if x1 == '':
        x1 = 0
    else:
        x1 = int(x1)
    
    if x2 == '':
        x2 = 0
    else:
        x2 = int(x2)
    
    result = x1 + x2
    return render_template('lab4/sum.html', x1=x1, x2=x2, result=result, back_link='/lab4/sum-form')

@lab4.route('/lab4/mul-form')
def mul_form():
    return render_template('lab4/mul-form.html')

@lab4.route('/lab4/mul', methods=['POST'])
def mul():
    x1 = request.form.get('x1', 1)
    x2 = request.form.get('x2', 1)
    
    if x1 == '':
        x1 = 1
    else:
        x1 = int(x1)
    
    if x2 == '':
        x2 = 1
    else:
        x2 = int(x2)
    
    result = x1 * x2
    return render_template('lab4/mul.html', x1=x1, x2=x2, result=result, back_link='/lab4/mul-form')

@lab4.route('/lab4/sub-form')
def sub_form():
    return render_template('lab4/sub-form.html')

@lab4.route('/lab4/sub', methods=['POST'])
def sub():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    
    if x1 == '' or x2 == '':
        return render_template('lab4/sub.html', error='Оба поля должны быть заполнены!', back_link='/lab4/sub-form')
    
    x1 = int(x1)
    x2 = int(x2)
    
    result = x1 - x2
    return render_template('lab4/sub.html', x1=x1, x2=x2, result=result, back_link='/lab4/sub-form')

@lab4.route('/lab4/pow-form')
def pow_form():
    return render_template('lab4/pow-form.html')

@lab4.route('/lab4/pow', methods=['POST'])
def pow():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    
    if x1 == '' or x2 == '':
        return render_template('lab4/pow.html', error='Оба поля должны быть заполнены!', back_link='/lab4/pow-form')
    
    x1 = int(x1)
    x2 = int(x2)
    
    if x1 == 0 and x2 == 0:
        return render_template('lab4/pow.html', error='Оба поля не могут быть нулями!', back_link='/lab4/pow-form')
    
    result = x1 ** x2
    return render_template('lab4/pow.html', x1=x1, x2=x2, result=result, back_link='/lab4/pow-form')

tree_count = 0

@lab4.route('/lab4/tree', methods=['GET', 'POST'])
def tree():
    global tree_count
    if request.method == 'GET':
        return render_template('lab4/tree.html', tree_count=tree_count)

    operation = request.form.get('operation')

    if operation == 'cut':
        if tree_count > 0:
            tree_count -= 1
    elif operation == 'plant':
        if tree_count < 10:  # Вы можете изменить это число на любое другое
            tree_count += 1

    return redirect('/lab4/tree')

users = [
    {"login": 'alex', "name": 'Alexander Smith', "gender": 'male', 'password': '123'},
    {"login": 'bob', "name": 'Bob Johnson', "gender": 'male', 'password': '555'},
    {"login": 'john', "name": 'John Doe', "gender": 'male', 'password': '777'},
    {"login": 'kenny', "name": 'Kenny Williams', "gender": 'male', 'password': '888'},
]

grain_prices = {
    'ячмень': 12345,
    'овёс': 8522,
    'пшеница': 8722,
    'рожь': 14111
}

@lab4.route('/lab4/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        authorized = 'login' in session
        login = session.get('login', '')
        name = ''
        if authorized:
            for user in users:
                if user['login'] == login:
                    name = user['name']
                    break
        return render_template('lab4/login.html', authorized=authorized, login=login, name=name)
    
    login = request.form.get('login')
    password = request.form.get('password')

    # Проверка на пустые значения
    if not login:
        error = 'Не введён логин'
        return render_template('lab4/login.html', error=error, authorized=False, login=login)
    if not password:
        error = 'Не введён пароль'
        return render_template('lab4/login.html', error=error, authorized=False, login=login)

    for user in users:
        if login == user['login'] and password == user['password']:
            session['login'] = login
            return redirect('/lab4/login')
    
    error = 'Неверные логин и/или пароль'
    return render_template('lab4/login.html', error=error, authorized=False, login=login)

@lab4.route('/lab4/logout', methods=['POST'])
def logout():
    session.pop('login', None)
    return redirect('/lab4/login')

@lab4.route('/lab4/fridge', methods=['GET', 'POST'])
def fridge():
    if 'login' not in session:
        return redirect('/lab4/login')

    if request.method == 'POST':
        if 'reset' in request.form:
            session.pop('fridge_temperature', None)
        else:
            temperature = request.form.get('temperature')
            if temperature:
                temperature = int(temperature)
                session['fridge_temperature'] = temperature

    temperature = session.get('fridge_temperature', None)
    message = ''
    snowflakes = 0

    if temperature is None:
        message = 'Ошибка: не задана температура'
    elif temperature < -12:
        message = 'Не удалось установить температуру — слишком низкое значение'
    elif temperature > -1:
        message = 'Не удалось установить температуру — слишком высокое значение'
    elif -12 <= temperature <= -9:
        message = f'Установлена температура: {temperature}°С'
        snowflakes = 3
    elif -8 <= temperature <= -5:
        message = f'Установлена температура: {temperature}°С'
        snowflakes = 2
    elif -4 <= temperature <= -1:
        message = f'Установлена температура: {temperature}°С'
        snowflakes = 1

    return render_template('lab4/fridge.html', message=message, snowflakes=snowflakes)

@lab4.route('/lab4/grain', methods=['GET', 'POST'])
def grain():
    if 'login' not in session:
        return redirect('/lab4/login')

    if request.method == 'POST':
        grain_type = request.form.get('grain_type')
        weight = request.form.get('weight')

        if not weight:
            error = 'Ошибка: не указан вес'
            return render_template('lab4/grain.html', error=error)

        weight = float(weight)

        if weight <= 0:
            error = 'Ошибка: вес должен быть больше 0'
            return render_template('lab4/grain.html', error=error)

        if weight > 500:
            error = 'Ошибка: такого объёма сейчас нет в наличии'
            return render_template('lab4/grain.html', error=error)

        price_per_ton = grain_prices.get(grain_type, 0)
        total_cost = price_per_ton * weight

        if weight > 50:
            discount = total_cost * 0.1
            total_cost -= discount
            discount_message = f'Применена скидка за большой объём: {discount:.2f} руб'
        else:
            discount_message = ''

        order_message = f'Заказ успешно сформирован. Вы заказали {grain_type}. Вес: {weight} т. Сумма к оплате: {total_cost:.2f} руб'
        return render_template('lab4/grain.html', order_message=order_message, discount_message=discount_message)

    return render_template('lab4/grain.html')
