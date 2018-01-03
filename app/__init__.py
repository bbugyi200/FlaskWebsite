""" app/__init__.py """

import sys
sys.path.insert(0, "/var/www/flasky/flasky")  # Needed before other imports

from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()


def create_app():
    from flask import Flask
    from config import config
    app = Flask(__name__, static_url_path='/app/static')
    app.config.from_object(config)
    config.init_app(app)

    bootstrap.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
