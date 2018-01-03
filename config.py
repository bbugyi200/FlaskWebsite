import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'bryanbugyi34@gmail.com'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    TRACK_USAGE_INCLUDE_OR_EXCLUDE_VIEWS = 'include'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    DEBUG = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {'development': DevelopmentConfig,
          'production': ProductionConfig,
          'default': DevelopmentConfig}[os.environ['FLASK_APP_CONFIG']]
