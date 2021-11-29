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

from app.admin.forms import NewsForm, ServiceForm
import base64


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
        form2 = NewsForm()

        services = Item.query.order_by(Item.created.desc()).all()
        news = Post.query.order_by(Post.created.desc()).all()
        users = User.query.order_by(User.created_on.desc()).all()
        roles = Role.query.order_by(Role.id.desc()).all()

        # for el in services:
        #     el.image = base64.b64encode(el.image).decode('ascii')
        # for el in news:
        #     el.image = base64.b64encode(el.image).decode('ascii')

        if form.validate_on_submit() or form2.validate_on_submit():

            if form.title2.data == "servises":
                title = form.title.data
                desc = form.desc.data
                url_serv = form.url_serv.data
                image = form.image.data.read()
                item = Item(title=title, desc=desc,
                            url_serv=url_serv, image=image)
            elif form2.title2.data == "news":
                title = form2.title.data
                desc = form2.desc.data
                body = form2.body.data
                image = form2.image.data.read()
                item = Post(title=title, desc=desc,
                            body=body, image=image)
            # elif form.title2.data is "projects":
            #     item = Item(title=title, desc=desc, url_serv=url_serv, image=image)

            try:
                db.session.add(item)
                db.session.commit()
                return redirect(url_for('.index'))
            except:
                return "error"

        if not current_user.has_role('admin'):
            if current_user.has_role('prepod'):
                return render_template("admin/prepod.html", form=form, form2=form2)
            else:
                return render_template("admin/kursant.html", form=form)

        # if request.method == "POST":

        return render_template("admin/index.html", form=form, form2=form2, services=services, users=users, roles=roles, news=news)

    @expose('/login/', methods=('GET', 'POST'))
    def login_page(self):
        if current_user.is_authenticated:
            return redirect(url_for('.index'))
        return super(MyAdminIndexView, self).index()

    @expose('/logout/')
    def logout_page(self):
        login.logout_user()
        return redirect(url_for('.index'))

    @expose('/reset/')
    def reset_page(self):
        return redirect(url_for('.index'))

    @expose('lk/user_settings/')
    def user_settings(self):
        return render_template("admin/user_settings.html",)


    @expose('service/<int:id>/del')
    def delete_service(self, id):
        service = Item.query.get_or_404(id)

        try:
            db.session.delete(service)
            db.session.commit()
            return redirect(url_for('.index'))
        except:
                return "error"

    @expose('news/<int:id>/del')
    def delete_news(self, id):
        news = Post.query.get_or_404(id)

        try:
            db.session.delete(news)
            db.session.commit()
            return redirect(url_for('.index'))
        except:
                return "error"


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
