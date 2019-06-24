import logging

from flask import Flask

from .config import app_config

from models import db

logger = logging.getLogger(__name__)


def create_app(env_name):
    """
    create application
    """

    # app initialization
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])

    db.init_app(app)

    # @app.route('/api/v1/brands', methods=['GET'])
    # def get_brands():
    #     brands = db.session.query(Brand).query.all()
    #     return jsonify([e.serialize() for e in brands])

    return app
