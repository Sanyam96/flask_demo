from flask import jsonify


def handle(product_id):
    return jsonify({
        'id': product_id
    })
