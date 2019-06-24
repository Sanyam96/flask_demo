from flask import Flask, request, json, Response, jsonify

from src.models import Brand


def get_brands():
    brands = Brand.Brand.query.all()
    return json.dumps(brands)
    # return jsonify([e.serialize() for e in brands])
