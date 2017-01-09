""" models.py

SQL Table Models """

from . import db


class Flask_Usage(db.Model):
    __tablename__ = 'flask_usage'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(128))
    ua_browser = db.Column(db.String(16))
    ua_language = db.Column(db.String(16))
    ua_platform = db.Column(db.String(16))
    ua_version = db.Column(db.String(16))
    blueprint = db.Column(db.String(16))
    view_args = db.Column(db.String(64))
    status = db.Column(db.Integer)
    remote_addr = db.Column(db.String(24))
    xforwardedfor = db.Column(db.String(24))
    authorization = db.Column(db.Boolean)
    ip_info = db.Column(db.String(128))
    path = db.Column(db.String(32))
    speed = db.Column(db.Float)
    datetime = db.Column(db.DateTime)
