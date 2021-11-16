import os
from flask import Flask
# from app import app

class Config(object):
    # ...

    # db_url = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # db_path = os.path.join(app.instance_path, "app.sqlite")
    # db_url = f"sqlite:///{db_path}"
    # # ensure the instance folder exists
    # os.makedirs(app.instance_path, exist_ok=True)

    SECRET_KEY=os.environ.get("SECRET_KEY", "dev")
    SQLALCHEMY_DATABASE_URI= "postgresql://flask_user:password@localhost:5432/flask"
    SQLALCHEMY_TRACK_MODIFICATIONS=False