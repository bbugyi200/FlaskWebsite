from . import main
from flask import render_template
from datetime import datetime


@main.route('/')
def home():
    try:
        return render_template('home.html', pagetype='home', current_time=datetime.utcnow())
    except Exception as E:
        return str(E)


@main.route('/about')
def about():
    return render_template('about.html', pagetype='about')

@main.route('/coursework')
def coursework():
    return render_template('coursework.html', pagetype='coursework')


@main.route('/resume')
def resume():
    return render_template('resume.html', pagetype='resume')
