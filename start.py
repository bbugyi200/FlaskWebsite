""" __init__.py

where it all begins...
"""

import os
import urllib.request
from threading import Timer

os.environ['FLASK_APP_CONFIG'] = 'production'

from manage import app
from werkzeug.debug import DebuggedApplication

# Enabling debugging
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)
app.debug = True


#######################################
#  Sets up Job to Fetch cv.pdf Daily  #
#######################################

this_dir = os.path.abspath(os.path.dirname(__file__))
cvPath = this_dir + "/app/static/resume/cv.pdf"


def fetchCVFromGitHub():
    resp = urllib.request.urlopen("http://github.com/bbugyi200/CV/raw/master/cv.pdf")

    file = open(cvPath, 'wb')
    file.write(resp.read())
    file.close()
    Timer(10800, fetchCVFromGitHub).start()


if __name__ == '__main__':
    app.run()
