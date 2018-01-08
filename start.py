""" __init__.py

where it all begins...
"""

import os
import atexit
import urllib.request

os.environ['FLASK_APP_CONFIG'] = 'production'

from manage import app
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from werkzeug.debug import DebuggedApplication

# Enabling debugging
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)
app.debug = True


#######################################
#  Sets up Job to Fetch cv.pdf Daily  #
#######################################

def fetchCVFromGitHub():
    this_dir = os.path.abspath(os.path.dirname(__file__))
    target = this_dir + "/app/static/resume/cv.pdf"
    resp = urllib.request.urlopen("http://github.com/bbugyi200/CV/raw/master/cv.pdf")

    file = open(target, 'wb')
    file.write(resp.read())
    file.close()


scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(func=fetchCVFromGitHub,
                  trigger=IntervalTrigger(hours=6),
                  id='fetch_cv_job',
                  name='Fetch cv.pdf from GitHub daily',
                  repace_existing=True)

atexit.register(lambda: scheduler.shutdown())


if __name__ == '__main__':
    app.run()
