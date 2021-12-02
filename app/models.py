from re import S
from flask import url_for, g

from datetime import datetime
from flask_login import UserMixin
from flask_security import RoleMixin
from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship, backref


from app import db


class roles_users(db.Model):
    __tablename__ = 'roles_user'
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String)
    user_id =  db.Column(db.Integer(), db.ForeignKey("user.id"))
    role_id =  db.Column(db.Integer(), db.ForeignKey("roles.id"))

    user = relationship("User", backref=backref("roles_user", cascade="all, delete-orphan"))
    product = relationship("Role", backref=backref("roles_user", cascade="all, delete-orphan"))


class Role(db.Model, RoleMixin):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))
    users = relationship("User", secondary="roles_user")

    def __str__(self):
        return self.name


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)
    # Нужен для security!
    active = db.Column(db.Boolean())
    # Для получения доступа к связанным объектам
    roles = relationship("Role", secondary="roles_user")

    # Flask - Login
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    # Flask-Security
    def has_role(self, *args):
        return set(args).issubset({role.name for role in self.roles})

    def get_id(self):
        return self.id

    # Required for administrative interface
    def __unicode__(self):
        return self.username

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


# Отвечает за сессию пользователей. Запрещает доступ к роутам, перед которыми указано @login_required
# @login_manager.user_loader
# def load_user(user_id):
#     if db.session["user_id"]:
#         user = User.query.filter_by(username=db.session["user_id"]).first()
#     else:
#         user = {"name": "Guest"}  # Make it better, use an anonymous User instead

#     g.user = user
#     return db.session.query(User).get(user_id)

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    created = db.Column(
        db.DateTime, nullable=False, server_default=db.func.current_timestamp()
    )
    desc = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable=False)
    image = db.Column(db.LargeBinary)

    @property
    def update_url(self):
        return url_for("site.update", id=self.id)

    @property
    def delete_url(self):
        return url_for("site.delete", id=self.id)



class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    created = db.Column(
        db.DateTime, nullable=False, server_default=db.func.current_timestamp()
    )
    desc = db.Column(db.String, nullable=False)
    url_serv = db.Column(db.String, nullable=False)
    image = db.Column(db.LargeBinary)
    active = db.Column(db.Boolean())

    def __repr__(self):
        return self.title



class Project(db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    created = db.Column(
        db.DateTime, nullable=False, server_default=db.func.current_timestamp()
    )
    desc = db.Column(db.String, nullable=False)
    url_serv = db.Column(db.String, nullable=False)
    image = db.Column(db.LargeBinary)
    active = db.Column(db.Boolean())

    def __repr__(self):
        return self.title




# Отвечает за сессию пользователей. Запрещает доступ к роутам, перед которыми указано @login_required
@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)