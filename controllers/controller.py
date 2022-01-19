from flask import render_template
from app import app
from models.orders import orders

@app.route('/')
def index():
    return render_template('index.html', open_orders = orders)

@app.route('/orders/<number>')
def order(number):
    return render_template('order.html', single_order = orders[int(number)])