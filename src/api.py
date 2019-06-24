from src.views import index, product_view, ProductView, brand_view


def url(app):
    app.add_url_rule('/api/v1', 'index', index.handle)
    app.add_url_rule('/api/v1/product/<int:product_id>', 'product', product_view.handle)
    app.add_url_rule('/api/v1/products', 'get_brands', ProductView.get_brands)
    # app.add_url_rule('/brands', 'get_brands', brand_view.get_brands)
    app.add_url_rule('/api/v1/savebrand', 'save_brand', brand_view.save_brand, methods=['POST'])
    app.add_url_rule('/api/v1/deletebrand')
    app.add_url_rule('/api/v1/products')
    app.add_url_rule('/api/v1/products/<int:product_id>')
    app.add_url_rule('/api/v1/products?sort_by=brands')
    app.add_url_rule('/api/v1/products?sort_by=price')
    app.add_url_rule('/api/v1/categories')
    app.add_url_rule('/api/v1/savecategory')
    app.add_url_rule('/api/v1/deletecategory')
