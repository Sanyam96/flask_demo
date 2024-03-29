from flask import Flask, request, Response, jsonify, json

from src.models import Brand
from src.models import db
from src.models.Brand import BrandSchema


def get_brands():
    # brands = Brand.Brand.query.all()
    brands = Brand.Brand.query.all()
    print (brands)
    print (type(brands))
    schema = BrandSchema()
    return jsonify(map(schema.dump, brands))
    # for e in brands:
    #     print(e.serialize())
    # return json.dumps([e.serialize() for e in brands])
    # return jsonify(json.dumps(brands))

    # return json.dumps(brands)
    # return Response(json.dumps(brands), mimetype='application/json')
    # return jsonify(results = brands)
    # return jsonify([e.serialize() for e in brands])


def save_brand():
    name = request.form.get('name')
    brand = Brand.Brand(
        name=name
    )
    # db.create_all(brand)
    db.session.add(brand)
    db.session.commit()

    return "Brand added, brand id = {}".format(brand.id)


def update_brand(brand_id):
    name = request.form.get('name')
    brand = Brand.Brand.query.get(brand_id)
    brand.name = name
    db.session.add(brand)
    db.session.commit()
    return "Brand Updated"


def delete_brand(brand_id):
    db.session.delete(brand_id)
    db.session.commit()
    return "Brand deleted"
