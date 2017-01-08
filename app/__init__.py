import sys
sys.path.insert(0, "/var/www/flasky/flasky")  # Needed before other imports

from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    from flask import Flask
    from config import config
    app = Flask(__name__, static_url_path='/app/static')
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from flask_track_usage import TrackUsage
    from flask_track_usage.storage.printer import PrintStorage

    bootstrap.init_app(app)
    db.init_app(app)

    from main import main as main_blueprint
    from main.views import home, about, resume, contact, image
    app.register_blueprint(main_blueprint)
    t = TrackUsage(app, PrintStorage())

    t.include(home)
    t.include(about)
    t.include(resume)
    t.include(contact)
    t.include(image)

    return app
