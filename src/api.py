from src.views import index, product_view, ProductView


def url(app):
    app.add_url_rule('/', 'index', index.handle)
    app.add_url_rule('/product/<int:product_id>', 'product', product_view.handle)
    app.add_url_rule('/products', 'get_brands', ProductView.get_brands)
