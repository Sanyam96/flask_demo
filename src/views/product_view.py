from flask import jsonify

from src.models import Product
from src.models import db


def handle(product_id):
    return jsonify({
        'id': product_id
    })


def get_all_products():
    products = Product.Product.query.all()
    return jsonify([e.serialize() for e in products])


def get_product(product_id):
    product = Product.Product.query.get(product_id)
    return product


def delete_product(product_id):
    db.session.delete(product_id)
    return "product deleted"


def get_products_sort_by(sort_by_param):
    if sort_by_param == 'price':
        products = Product.Product.query.orderby('price').all()
        return jsonify([e.serialize() for e in products])
