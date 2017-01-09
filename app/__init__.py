""" app/__init__.py """

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
    from flask_track_usage.storage.sql import SQLStorage

    bootstrap.init_app(app)
    db.init_app(app)

    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    UsageData = 0
    from main.views import home, about, resume, contact, image
    with app.app_context():
        UsageData = SQLStorage(db=db)
        tu = TrackUsage(app, UsageData)

        tu.include(home)
        tu.include(about)
        tu.include(resume)
        tu.include(contact)
        tu.include(image)

    return app, UsageData
