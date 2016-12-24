import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'bryanbugyi34@gmail.com'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'bryanbugyi34@gmail.com'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URL = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {'development': DevelopmentConfig,
          'testing': TestingConfig,
          'production': ProductionConfig,
          'default': DevelopmentConfig}
