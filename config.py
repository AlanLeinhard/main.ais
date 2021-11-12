import os

class Config(object):
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fsDFKsmf923jnagd'
    SQLALCHEMY_DATABASE_URI = 'postgresql://user:pass/test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ################
    # Flask-Security
    ################

    SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
    SECURITY_PASSWORD_SALT = "fsdfk3fsdDFFdfsr0fsa"