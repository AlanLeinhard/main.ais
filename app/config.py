import os
basedir = os.path.abspath(os.path.dirname('instace'))

class Config(object):
    # ...
    SQLALCHEMY_TRACK_MODIFICATIONS = False