# import os
from app import create_app  # , db
from flask_script import Manager  # , Shell
from flask import Flask, url_for
import os

app = create_app('default')


###################################
#  CACHE BUSTER FOR STATIC FILES  #
###################################

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

##################################

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
