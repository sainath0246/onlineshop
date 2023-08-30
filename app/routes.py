# app/routes.py
from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Product, Order
import razorpay

client = razorpay.Client(auth=(app.config['RAZORPAY_KEY_ID'], app.config['RAZORPAY_KEY_SECRET']))

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/checkout/<int:product_id>')
def checkout(product_id):
    product = Product.query.get(product_id)
    amount_in_paise = int(product.price * 100)  # Convert rupees to paise

    order_data = {
        'amount': amount_in_paise,
        'currency': 'INR',
        'receipt': 'order_receipt',
        'payment_capture': 1
    }

    order = client.order.create(data=order_data)
    new_order = Order(product_id=product.id, amount=product.price)
    db.session.add(new_order)
    db.session.commit()

    return render_template('checkout.html', product=product, order=order)

if __name__ == '__main__':
    app.run(debug=True)
