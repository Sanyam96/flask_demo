import datetime
from . import db


class Product(db.Model):
    """
    Product Model
    """
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    discount = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('brands.id'), nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('categories.is'), nullable=False)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.name = data.get('name')
        self.price = data.get('price')
        self.quantity = data.get('quantity')
        self.discount = data.get('discount')
        # todo
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def __repr(self):
        return '<id {}>'.format(self.id)
