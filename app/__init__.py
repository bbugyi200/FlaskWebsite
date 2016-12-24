import sys
sys.path.insert(0, "/var/www/flasky/flasky")  # Needed before other imports

from flask import Flask
from flask_bootstrap import Bootstrap
from config import config


bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__, static_url_path='/app/static')
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)

    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
