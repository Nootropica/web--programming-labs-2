from flask import Blueprint, render_template, request, make_response, redirect, url_for
lab3 = Blueprint('lab3', __name__)

# Список товаров (смартфоны)
products = [
    {"name": "iPhone 13", "price": 999, "brand": "Apple", "memory": "128GB"},
    {"name": "Samsung Galaxy S21", "price": 899, "brand": "Samsung", "memory": "128GB"},
    {"name": "Google Pixel 6", "price": 699, "brand": "Google", "memory": "128GB"},
    {"name": "OnePlus 9", "price": 799, "brand": "OnePlus", "memory": "128GB"},
    {"name": "Xiaomi Mi 11", "price": 699, "brand": "Xiaomi", "memory": "128GB"},
    {"name": "Sony Xperia 1 III", "price": 1199, "brand": "Sony", "memory": "256GB"},
    {"name": "Huawei P40 Pro", "price": 899, "brand": "Huawei", "memory": "256GB"},
    {"name": "LG Velvet", "price": 599, "brand": "LG", "memory": "128GB"},
    {"name": "Motorola Edge", "price": 699, "brand": "Motorola", "memory": "256GB"},
    {"name": "Nokia 8.3", "price": 499, "brand": "Nokia", "memory": "128GB"},
    {"name": "Oppo Find X3 Pro", "price": 1099, "brand": "Oppo", "memory": "256GB"},
    {"name": "Realme GT", "price": 599, "brand": "Realme", "memory": "128GB"},
    {"name": "Vivo X60 Pro", "price": 799, "brand": "Vivo", "memory": "256GB"},
    {"name": "ZTE Axon 30", "price": 499, "brand": "ZTE", "memory": "128GB"},
    {"name": "Asus ROG Phone 5", "price": 999, "brand": "Asus", "memory": "256GB"},
    {"name": "BlackBerry Key2", "price": 699, "brand": "BlackBerry", "memory": "128GB"},
    {"name": "HTC U12+", "price": 599, "brand": "HTC", "memory": "128GB"},
    {"name": "Lenovo Legion Phone Duel", "price": 899, "brand": "Lenovo", "memory": "256GB"},
    {"name": "Meizu 18", "price": 699, "brand": "Meizu", "memory": "128GB"},
    {"name": "TCL 20 Pro 5G", "price": 499, "brand": "TCL", "memory": "256GB"}
]


@lab3.route('/lab3/')
def labb():
    name = request.cookies.get('name') or 'аноним'
    age = request.cookies.get('age') or 'неизвестный'
    name_color = request.cookies.get('name_color')
    return render_template('lab3.html', name=name, name_color=name_color, age=age)


@lab3.route('/lab3/cookie/')
def cookie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name', 'Alex', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('name_color', 'magenta')
    return resp


@lab3.route('/lab3/del_cookies/')
def del_cookies():
    resp = make_response(redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    return resp
    

@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
        
    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'

    sex = request.args.get('sex')
    return render_template('lab3/form1.html', user=user, age=age, sex=sex, errors=errors)


@lab3.route('/lab3/order')
def order():
    return render_template('lab3/order.html')

@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'coffee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10

    # Сохраняем значение цены в куки
    resp = make_response(render_template('lab3/pay.html', price=price))
    resp.set_cookie('price', str(price))
    return resp


@lab3.route('/lab3/success')
def success():
    price = request.cookies.get('price')  # Получаем цену из куки
    return render_template('lab3/success.html', price=price)


@lab3.route('/lab3/settings', methods=["GET", "POST"])
def settings():
    if request.method == "POST":
        color = request.form.get('color')
        background_color = request.form.get('background_color')
        font_size = request.form.get('font_size')

        resp = make_response(redirect('/lab3/settings'))

        if color:
            resp.set_cookie('color', color)
        if background_color:
            resp.set_cookie('background_color', background_color)
        if font_size:
            resp.set_cookie('font_size', font_size)

        return resp

    # Если метод GET, получаем значения из cookies
    color = request.cookies.get('color')
    background_color = request.cookies.get('background_color')
    font_size = request.cookies.get('font_size')
    
    return render_template('/lab3/settings.html', color=color, background_color=background_color, font_size=font_size)


@lab3.route('/lab3/ticket', methods=['GET', 'POST'])
def ticket():
    if request.method == 'POST':
        fio = request.form.get('fio')
        age = int(request.form.get('age'))
        bunk = request.form.get('bunk')
        bedding = 'bedding' in request.form
        baggage = 'baggage' in request.form
        departure = request.form.get('departure')
        destination = request.form.get('destination')
        date = request.form.get('date')
        insurance = 'insurance' in request.form

        errors = {}
        if not fio:
            errors['fio'] = 'Заполните поле!'
        if age < 1 or age > 120:
            errors['age'] = 'Возраст должен быть от 1 до 120 лет!'
        if not departure:
            errors['departure'] = 'Заполните поле!'
        if not destination:
            errors['destination'] = 'Заполните поле!'
        if not date:
            errors['date'] = 'Заполните поле!'

        if errors:
            return render_template('lab3/ticket_form.html', errors=errors)

        base_price = 700 if age < 18 else 1000
        if bunk in ['lower', 'lower_side']:
            base_price += 100
        if bedding:
            base_price += 75
        if baggage:
            base_price += 250
        if insurance:
            base_price += 150

        return render_template('lab3/ticket.html', fio=fio, age=age, bunk=bunk, bedding=bedding, baggage=baggage, departure=departure, destination=destination, date=date, insurance=insurance, price=base_price)

    return render_template('lab3/ticket_form.html', errors={})


@lab3.route('/lab3/clear_all_cookies/')
def clear_all_cookies():
    response = make_response(redirect(url_for('lab3.labb')))
    response.delete_cookie('name')
    response.delete_cookie('age')
    response.delete_cookie('name_color')
    response.delete_cookie('color')
    response.delete_cookie('background_color')
    response.delete_cookie('font_size')
    return response


@lab3.route('/lab3/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        min_price = float(request.form.get('min_price', 0))
        max_price = float(request.form.get('max_price', float('inf')))

        filtered_products = [product for product in products if min_price <= product['price'] <= max_price]
        return render_template('lab3/search_results.html', products=filtered_products)

    return render_template('lab3/search_form.html')




