from flask import Blueprint, render_template
import base64

from app.models import Item, Post

bp = Blueprint("site", __name__)


@bp.route("/")
def index():
    """Show all the posts, most recent first."""
    post = Post.query.order_by(Post.created.desc()).all()
    item = Item.query.order_by(Item.created.desc()).all()

    for el in post:
        el.image = base64.b64encode(el.image).decode('ascii')

    for el in item:

        el.image = base64.b64encode(el.image).decode('ascii')

    return render_template("site/index.html", data=list, item=item, post=post)

@bp.route("/<int:id>")
def news(id):
    """Show all the posts, most recent first."""
    post = Post.query.get_or_404(id)
    post.image = base64.b64encode(post.image).decode('ascii')
    return render_template("site/news.html", post=post)
