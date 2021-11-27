from flask import Blueprint, render_template
import base64

from wtforms.form import Form

from app.models import Item, Post
from app.site.forms import  SearchForm

bp = Blueprint("site", __name__)


@bp.route('/', methods=['POST', 'GET'])
def index():
    """Show all the posts, most recent first."""
    form = SearchForm()
    post = Post.query.order_by(Post.created.desc()).all()
    item = Item.query.order_by(Item.created.desc()).all()

    if form.validate_on_submit():
        print("asdfdgf")
        print(form.select.data)
        print(form.search.data)

    for el in post:
        el.image = base64.b64encode(el.image).decode('ascii')

    for el in item:

        el.image = base64.b64encode(el.image).decode('ascii')

    

    return render_template("site/index.html", data=list, item=item, post=post, form=form)

@bp.route("/<int:id>")
def news(id):
    """Show all the posts, most recent first."""
    post = Post.query.get_or_404(id)
    post.image = base64.b64encode(post.image).decode('ascii')
    return render_template("site/news.html", post=post)
