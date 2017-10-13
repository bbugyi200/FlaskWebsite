""" __init__.py

where it all begins...
"""
from manage import app, db
from app.models import Flask_Usage

# Enabling debugging
from werkzeug.debug import DebuggedApplication
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)
app.debug = True

if __name__ == '__main__':
    db.create_all()
    app.run()
