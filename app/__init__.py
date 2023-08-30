# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

app.config['RAZORPAY_KEY_ID'] = RAZORPAY_KEY_ID
app.config['RAZORPAY_KEY_SECRET'] = RAZORPAY_KEY_SECRET

from app import routes
