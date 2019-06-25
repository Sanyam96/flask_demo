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

    # Foreign Keys
    category_id = db.Column(db.Integer, db.ForeignKey('brands.id'), nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    # category = db.relationship('Category', backref=db.backref('products', lazy='dynamic'))
    # brand = db.relationship('Brand', backref=db.backref('products', lazy='dynamic'))

    # class constructor
    # def __init__(self, data):
    #     """
    #     Class constructor
    #     """
    #     self.name = data.get('name')
    #     self.price = data.get('price')
    #     self.quantity = data.get('quantity')
    #     self.discount = data.get('discount')
    #
    #     # todo check -> brand and category id
    #     self.brand_id = data.get('brand_id')
    #     self.category_id = data.get('category_id')
    #
    #     self.created_at = datetime.datetime.utcnow()
    #     self.modified_at = datetime.datetime.utcnow()

    def __init__(self, name, price, quantity, discount, brand_id, category_id):
        """
        Class constructor
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.discount = discount

        # todo check -> brand and category id
        self.brand_id = brand_id
        self.category_id = category_id

        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def __repr(self):
        return '<id {}>'.format(self.id)

