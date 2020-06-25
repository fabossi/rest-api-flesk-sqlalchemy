from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))


# Databse

app.config['SQLALCHEMY_DATABSE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initi DB

db = SQLAlchemy(app)

# Init Marshmallow

marsh = Marshmallow(app)


# Products Class - Model 

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.column(db.Float)
    qty = db.column(db.Integer)


def __init__(self, name, description, price, qty):
    self.name = name
    self.description = description
    self.prince = prince
    self.qty = qty


# Run Server

if __name__ == '__main__':
    app.run(debug=True)