""" __init__.py

where it all begins...
"""
from manage import app
import os # master

# Enabling debugging
from werkzeug.debug import DebuggedApplication
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)
app.debug = True

if __name__ == '__main__':
    app.run()
