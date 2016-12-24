from . import main
from flask import render_template


@main.route('/')
def home():
    try:
        return render_template('home.html', pagetype='home')
    except Exception as E:
        return str(E)


@main.route('/about')
def about():
    return render_template('about.html', pagetype='about')


@main.route('/resume')
def resume():
    return render_template('resume.html', pagetype='resume')
