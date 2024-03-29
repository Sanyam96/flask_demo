import os

from src.app import create_app
from src.api import url

env_name = os.getenv('FLASK_ENV')
app = create_app(env_name)

url(app)

if __name__ == '__main__':
    app.run()
