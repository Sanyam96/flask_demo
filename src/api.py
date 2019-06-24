from src.views import index, product_view, ProductView, brand_view


def url(app):
    app.add_url_rule('/', 'index', index.handle)
    app.add_url_rule('/product/<int:product_id>', 'product', product_view.handle)
    app.add_url_rule('/products', 'get_brands', ProductView.get_brands)
    # app.add_url_rule('/brands', 'get_brands', brand_view.get_brands)
    app.add_url_rule('/savebrand', 'save_brand', brand_view.save_brand, methods=['POST'])
