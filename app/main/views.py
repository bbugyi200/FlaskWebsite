import getpass
import urllib.request

from . import main
from flask import render_template, send_from_directory


@main.route('/')
def home():
    try:
        return render_template('home.html', pagetype='home')
    except Exception as E:
        return str(E)


@main.route('/contact')
def contact():
    return render_template('contact.html', pagetype='contact')


@main.route('/resume')
def resume():
    cvPath = "/home/" + getpass.getuser() + "/Website/app/static/resume/cv.pdf"

    def fetchCVFromGitHub():
        resp = urllib.request.urlopen("http://github.com/bbugyi200/CV/raw/master/cv.pdf")

        file = open(cvPath, 'wb')
        file.write(resp.read())
        file.close()

    fetchCVFromGitHub()

    return render_template('resume.html', pagetype='resume')


@main.route('/img/<img>')
def image(img):
    return render_template('image.html',
                           pagetype='image',
                           image='img/%s' % img)


@main.route('/files/<F>')
def file(F):
    return send_from_directory(directory='static/files',
                               filename=F,
                               as_attachment=True)


@main.route('/bookoftheweek')
def bookoftheweek():
    return send_from_directory(directory='static/books',
                               filename='ProGit.pdf',
                               as_attachment=True)
