from flask import Flask, render_template, make_response, request, redirect, abort, session, url_for, flash
from flask_script import Manager, Shell
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from flask_migrate import Migrate, MigrateCommand
from flask_mail import Mail, Message


import os
import sys
from datetime import datetime
from threading import Thread

# WTForms Imports
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required

app = Flask(__name__)

# Enabling debugging
from werkzeug.debug import DebuggedApplication
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)
app.debug = True

# SQLAlchemy Database Setup
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

# ------------ Email Configurations ------------------
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'bryanbugyi34@gmail.com'
app.config['MAIL_PASSWORD'] = 'KellyDee33'
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = 'bryanbugyi34@gmail.com'
app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')
# ----------------------------------------------------


bootstrap = Bootstrap(app)
manager = Manager(app)
moment = Moment(app)
migrate = Migrate(app, db)
mail = Mail(app)

manager.add_command('db', MigrateCommand)


# ------------ Email Sending Functions ---------------
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'],
                  recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr
# ----------------------------------------------------

# --------- Database Columns -----------
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
       return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.name

if os.path.isfile('/var/www/flasky/flasky/data.sqlite'):
    usr = Role.query.filter_by(name='User').first()
    if usr is None:
        usr = Role(name='User')
# --------------------------------------


#-------------- Shell configuration --------------
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)

manager.add_command("shell", Shell(make_context=make_shell_context))
# ------------------------------------------------



######################
#  Official Content  #
######################


@app.route('/')
def home():
    try: 
        return render_template('home.html', pagetype="home", current_time=datetime.utcnow())
    except Exception as E:
        return str(E)


@app.route('/about')
def about():
    try:
        return render_template('about.html', pagetype="about")
    except Exception as E:
        return str(E)


@app.route('/coursework')
def coursework():
    try:
        return render_template('coursework.html', pagetype="coursework")
    except Exception as E:
        return str(E)


@app.route('/resume')
def resume():
    try:
        return render_template('resume.html', pagetype="resume")
    except Exception as E:
        return str(E)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# @app.errorhandler(Exception)
# def exception_handler(e):
#     return "Exception Type: " + str(sys.exc_info()) + "<br>Args: " +  str(e.args[0])



##################
#  Test Content  #
##################


@app.route('/user/<name>')
def user(name):
    listofnames = ['Bryan', 'Matt', 'David', 'Johny', 'Sean']
    if name not in listofnames:
        abort(404)
    return render_template('base.html', toptitle='Welcome '+name)


@app.route('/setcookie')
def setcookie():
    try:
        if 'bryan' in request.cookies:
            return render_template('base.html', toptitle='You already have a cookie!')
        else:
            response = make_response(render_template('base.html',
                                    toptitle='A cookie has been set! Muhaha Muhahahahahahahahah!!!'))
            response.set_cookie('bryan', value='awesome')
            return response
    except Exception as E:
        return str(E)


@app.route('/google')
def google():
    return redirect('http://www.google.com')


@app.route('/complextypes')
def ctypes():
    var = ctypes.mylist.pop(0)
    ctypes.mylist.append(var)
    return render_template('complextypes.html', mylist=ctypes.mylist)
ctypes.mylist = ['cats', 'dogs', 'pigs'] 


@app.route('/macrotest')
def macrotext():
    items = ['Math', 'Humanities', 'Computer Science', 'Physical Science']
    return render_template('macrotest.html', items=items)


class LoginForm(Form):
    username = StringField('Username: ', validators=[Required()])
    password = PasswordField('Password: ', validators=[Required()])
    login = SubmitField('Login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(name=form.username.data).first()
        if user is None:
            user = User(name=form.username.data, role=usr)
            db.session.add(user)
            session['known'] = False
            send_email('bryan_bugyi@mymail.bcc.edu',
                       "New User",
                       'mail/new_user', user=user)
        else:
            session['known'] = True

        old_name = session.get('name')
        if old_name is not None and old_name != form.username.data:
            flash("You've changed your name!")
        session['name'] = form.username.data
        form.username.data = ''
        return redirect(url_for('login'))
    return render_template('login.html', form=form, name=session.get('name'),
                           known=session.get('known'))



if __name__ == '__main__':
    manager.run()
    from flask_mail import Message
    msg = Message('test subject', sender='me@example.com', recipients=['bryan_bugyi@mymail.bcc.edu'])
    msg.body = 'text body'
    msg.html = '<b>HTML</b> body'
    with app.app_context():
        mail.send(msg)
