from flask import jsonify, request

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
    product = Product.Product.query.get(product_id)
    db.session.delete(product)
    db.session.commit()
    return "product deleted"


def get_products_sort_by(sort_by_param):
    if sort_by_param == 'price':
        products = Product.Product.query.orderby('price').all()
        return jsonify([e.serialize() for e in products])


def add_product():
    name = request.form.get('name')
    price = request.form.get('price')
    quantity = request.form.get('quantity')
    discount = request.form.get('discount')
    brand_id = request.form.get('brand_id')
    category_id = request.form.get('category_id')
    product = Product.Product(
        name=name,
        price=price,
        quantity=quantity,
        discount=discount,
        brand_id=brand_id,
        category_id=category_id
    )
    db.session.add(product)
    db.session.commit()

    return "Product added, product id = {}".format(product.id)

