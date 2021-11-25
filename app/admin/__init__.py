from re import match
from flask.templating import render_template
from app import db, app
from flask import url_for, redirect, request, abort
from app.models import Post, User, Role, Item

# flask-login
from flask_login import current_user
import flask_login as login

# flask-security
from flask_security import SQLAlchemyUserDatastore, Security

# flask-admin
import flask_admin
from flask_admin import helpers, expose
from flask_admin.contrib import sqla

import os
from werkzeug.utils import secure_filename

from app.admin.forms import ServiceForm, RegisterForm, LoginForm


# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


# Create customized model view class
class MyModelView(sqla.ModelView):

    def is_accessible(self):
        return (current_user.is_active and
                current_user.is_authenticated and
                current_user.has_role('admin')
                )

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                return redirect(url_for('security.login', next=request.url))


# Переадресация страниц (используется в шаблонах)
class MyAdminIndexView(flask_admin.AdminIndexView):
    @expose('/', methods=['POST', 'GET'])
    def index(self):
        if not current_user.is_authenticated:
            return redirect(url_for('.login_page'))

        form = ServiceForm()
        if form.validate_on_submit():
            title = form.title.data
            desc = form.desc.data
            url_serv = form.url_serv.data
            image = form.image.data.read()
            # print(image)


            if form.title2.data == "servises":
                item = Item(title=title, desc=desc, url_serv=url_serv, image=image)
            elif form.title2.data == "news":
                item = Post(title=title, desc=desc, url_serv=url_serv, image=image)
            # elif form.title2.data is "projects":
            #     item = Item(title=title, desc=desc, url_serv=url_serv, image=image)



                

            try:
                db.session.add(item)
                db.session.commit()
            except:
                return super(MyAdminIndexView, self).index()

        # if request.method == "POST":

        return render_template("admin/index.html", form=form)

    # def create(self):
    #     if request.method == "POST":
    #         title = request.form['title']
    #         desc = request.form['desc']
    #         url_serv = request.form['url_serv']
    #         image = request.form['image']

    #         item = Item(title=title, desc=desc,url_serv=url_serv)

    #         try:
    #             db.session.add(item)
    #             db.session.commit()
    #             return "true"
    #         except:
    #             return "error"

    #     else:
    #         return super(MyAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_page(self):
        if current_user.is_authenticated:
            return redirect(url_for('.index'))

        # создаем экземпляр класса формы
        form = LoginForm(request.form)
        # если HTTP-метод POST и данные формы валидны
        if form.validate_on_submit():
            # используя схему `SQLAlchemy` создаем объект,
            # для последующей записи в базу данных
            user = User(form.username.data,
                        form.password.data)
            db.session.add(user)
            return redirect(url_for('login'))
        # если HTTP-метод GET, то просто отрисовываем форму
        return render_template('register.html', form=form)
        return super(MyAdminIndexView, self).index()

    @expose('/logout/')
    def logout_page(self):
        login.logout_user()
        return redirect(url_for('.index'))

    @expose('/reset/')
    def reset_page(self):
        return redirect(url_for('.index'))

    @expose('/register', methods=['GET', 'POST'])
    def register():
        # создаем экземпляр класса формы
        form = RegisterForm(request.form)
        # если HTTP-метод POST и данные формы валидны
        if form.validate_on_submit():
            # используя схему `SQLAlchemy` создаем объект,
            # для последующей записи в базу данных
            user = User(form.username.data, form.email.data,
                        form.password.data)
            db.session.add(user)
            return redirect(url_for('login'))
        # если HTTP-метод GET, то просто отрисовываем форму
        return render_template('register.html', form=form)


# Create admin
admin = flask_admin.Admin(app, index_view=MyAdminIndexView(
), base_template='admin/master-extended.html')

# Add view
admin.add_view(MyModelView(User, db.session))
# admin.add_view(MyModelView(UserSetting, db.session))

# define a context processor for merging flask-admin's template context into the
# flask-security views.


@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        h=helpers,
        get_url=url_for
    )
