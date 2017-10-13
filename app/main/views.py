from . import main
from flask import render_template


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
    return render_template('resume.html', pagetype='resume')


@main.route('/img/<img>')
def image(img):
    return render_template('image.html',
                           pagetype='image',
                           image='img/%s' % img)
