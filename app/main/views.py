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
                               filename='Practical_Vim-(Neil).pdf',
                               as_attachment=True)
