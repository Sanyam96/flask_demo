import datetime
from marshmallow import Schema, fields, pre_load, validate
from . import db
from . import ma


class Category(db.Model):
    """
    Category Model
    """
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    # One to Many relationship between Categories and Product
    """
    Each product belongs to a single category, but each categories may have multiple products
    """
    products = db.relationship('Product', backref="categories", lazy='dynamic')

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


class CategorySchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
