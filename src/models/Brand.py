import datetime
from marshmallow import Schema, fields, pre_load, validate
from . import ma
from . import db


class Brand(db.Model):
    """
    Brand Model
    """
    __tablename__ = 'brands'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    # One to Many relationship between Brand and Products
    """
    Each product belongs to a single brand but every brands may multiple products
    """
    products = db.relationship('Product', backref="brands", lazy='dynamic')

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.name = data.get('name')
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def __repr(self):
        return '<id {}>'.format(self.id)


class BrandSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String()
