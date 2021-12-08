from flask.templating import render_template
from flask_login.utils import login_required
from app import db, app
from flask import url_for, redirect, request, abort
from app.models import Post, Project, User, Role, Item

# flask-login
from flask_login import current_user
import flask_login as login

# flask-security
from flask_security import SQLAlchemyUserDatastore, Security

# flask-admin
import flask_admin
from flask_admin import helpers, expose
from flask_admin.contrib import sqla

from app.admin.forms import NewsForm, ProjectForm, ServiceForm, ServiceUpdForm, UserForm
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
        form3 = ProjectForm()

        services = Item.query.order_by(Item.created.desc()).all()
        projects = Project.query.order_by(Project.created.desc()).all()
        news = Post.query.order_by(Post.created.desc()).all()
        users = User.query.order_by(User.created_on.desc()).all()
        roles = Role.query.order_by(Role.id.desc()).all()

        # for el in services:
        #     el.image = base64.b64encode(el.image).decode('ascii')
        # for el in projects:
        #     el.image = base64.b64encode(el.image).decode('ascii')
        # for el in news:
        #     el.image = base64.b64encode(el.image).decode('ascii')

        if form.validate_on_submit() or form2.validate_on_submit() or form3.validate_on_submit():

            if form.title2.data == "services":

                item = Item(title=form.title.data, desc=form.desc.data,
                            url_serv=form.url_serv.data, image=form.image.data.read(), click=0, active=True)

            elif form.title2.data == "news":
                item = Post(author_id=current_user.id, title=form2.title.data, desc=form2.desc.data,
                            body=form2.body.data, image=form2.image.data.read())

            elif form.title2.data == "projects":
                item = Project(author_id=current_user.id, title=form3.title.data, desc=form3.desc.data,
                            url_serv=form3.url_serv.data, image=form3.image.data.read(), click=0, active=True)

            try:
                db.session.add(item)
                db.session.commit()
                return redirect(url_for('.index'))
            except:
                return "error"

        # if request.method == "POST":

        return render_template("admin/index.html", form=form, form2=form2, form3=form3, services=services, users=users, roles=roles, news=news, projects=projects)

    @expose('/login/', methods=('GET', 'POST'))
    def login_page(self):
        if current_user.is_authenticated:
            return redirect(url_for('.index'))
        return super(MyAdminIndexView, self).index()

    @expose('/logout/')
    @login_required
    def logout_page(self):
        login.logout_user()
        return redirect(url_for('.index'))

    @expose('/reset/')
    def reset_page(self):
        return redirect(url_for('.index'))

    @expose('lk/user_settings/<int:id>', methods=['POST', 'GET'])
    @login_required
    def user_settings(self, id):

        if current_user.id != id:
            if not current_user.has_role('admin'):
                return redirect(url_for('.index'))

        form = UserForm()
        user = User.query.get_or_404(id)

        if form.validate_on_submit():

            try:
                user.name = form.name.data
                user.username = form.username.data
                user.email = form.email.data

                if form.check.data == True:
                    
                    user.password = form.password.data

                db.session.commit()
                return redirect(url_for(".index"))
            except:
                return "error"

        return render_template("admin/user_settings.html", form=form, user=user)

    @expose('user/<int:id>/del')
    @login_required
    def delete_user(self, id):
        
        if current_user.id != id:
            if not current_user.has_role('admin'):
                return redirect(url_for('.index'))

        user = User.query.get_or_404(id)
        try:
            db.session.delete(user)
            db.session.commit()
            return redirect(url_for('.index'))
        except:
            return "error"

    @expose('service/<int:id>/del')
    @login_required
    def delete_service(self, id):
        
        if not current_user.has_role('admin'):
            return redirect(url_for('.index'))

        service = Item.query.get_or_404(id)

        try:
            db.session.delete(service)
            db.session.commit()
            return redirect(url_for('.index'))
        except:
            return "error"

    @expose('service/<int:id>/onoff')
    @login_required
    def service_on_off(self, id):
        
        if not current_user.has_role('admin'):
            return redirect(url_for('.index'))

        service = Item.query.get_or_404(id)

        try:
            if service.active:
                service.active = False
            else:
                service.active = True
            db.session.commit()
            return redirect(url_for('.index'))
        except:
            return "error"

    @expose('service/<int:id>/upd', methods=['POST', 'GET'])
    @login_required
    def service_upd(self, id):
        
        if not current_user.has_role('admin'):
            return redirect(url_for('.index'))


        form = ServiceUpdForm()
        service = Item.query.get(id)
        title = "сервис"
        # service.image = base64.b64encode(service.image).decode('ascii')

        if form.validate_on_submit():

            try:
                service.title = form.title.data

                service.desc = form.desc.data

                service.url_serv = form.url_serv.data

                if form.check.data == True:
                    service.image = form.image.data.read()

                db.session.commit()
                return redirect(url_for(".index"))
            except:
                return "error"

        return render_template("admin/service_upd.html", form=form, service=service, title=title)

    @expose('project/<int:id>/del')
    @login_required
    def delete_project(self, id):
        project = Project.query.get_or_404(id)
        
        if current_user.id != project.author_id:
            if not current_user.has_role('admin'):
                return redirect(url_for('.index'))


        try:
            db.session.delete(project)
            db.session.commit()
            return redirect(url_for('.index'))
        except:
            return "error"

    @expose('project/<int:id>/onoff')
    @login_required
    def project_on_off(self, id):
        project = Project.query.get_or_404(id)
        
        if current_user.id != project.author_id:
            if not current_user.has_role('admin'):
                return redirect(url_for('.index'))


        try:
            if project.active:
                project.active = False
            else:
                project.active = True
            db.session.commit()
            return redirect(url_for('.index'))
        except:
            return "error"

    @expose('project/<int:id>/upd', methods=['POST', 'GET'])
    @login_required
    def project_upd(self, id):

        form = ServiceUpdForm()
        service = Project.query.get(id)
        title = "проект"
        # service.image = base64.b64encode(service.image).decode('ascii')
        
        if current_user.id != service.author_id:
            if not current_user.has_role('admin'):
                return redirect(url_for('.index'))


        if form.validate_on_submit():

            try:
                service.title = form.title.data

                service.desc = form.desc.data

                service.url_serv = form.url_serv.data

                if form.check.data == True:
                    service.image = form.image.data.read()

                db.session.commit()
                return redirect(url_for(".index"))
            except:
                return "error"

        return render_template("admin/service_upd.html", form=form, service=service, title=title)

    @expose('news/<int:id>/del')
    @login_required
    def delete_news(self, id):
        news = Post.query.get_or_404(id)
        
        if current_user.id != news.author_id:
            if not current_user.has_role('admin'):
                return redirect(url_for('.index'))


        try:
            db.session.delete(news)
            db.session.commit()
            return redirect(url_for('.index'))
        except:
            return "error"

    @expose('news/<int:id>/upd', methods=['POST', 'GET'])
    @login_required
    def news_upd(self, id):

        form = ServiceUpdForm()
        news = Post.query.get(id)
        title = "новост"
        # service.image = base64.b64encode(service.image).decode('ascii')
        
        if current_user.id != news.author_id:
            if not current_user.has_role('admin'):
                return redirect(url_for('.index'))


        if form.validate_on_submit():

            try:
                news.title = form.title.data

                news.desc = form.desc.data

                news.body = form.url_serv.data

                if form.check.data == True:
                    news.image = form.image.data.read()

                db.session.commit()
                return redirect(url_for(".index"))
            except:
                return "error"

        return render_template("admin/news_upd.html", form=form, news=news, title=title)

    @expose('role/<int:id>/del')
    @login_required
    def delete_role(self, id):
        
        if not current_user.has_role('admin'):
            return redirect(url_for('.index'))

        role = Role.query.get_or_404(id)

        try:
            db.session.delete(role)
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