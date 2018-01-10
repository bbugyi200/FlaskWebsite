""" __init__.py

where it all begins...
"""

import os

os.environ['FLASK_APP_CONFIG'] = 'production'

from manage import app
from werkzeug.debug import DebuggedApplication

# Enabling debugging
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)
app.debug = True


if __name__ == '__main__':
    app.run()
