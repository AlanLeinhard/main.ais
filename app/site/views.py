from flask import Blueprint, render_template
import base64

from app.models import Item, Post

bp = Blueprint("site", __name__)


@bp.route("/")
def index():
    """Show all the posts, most recent first."""
    post = Post.query.order_by(Post.created).all()
    items = Item.query.order_by(Item.created).all()
    for el in items:
        el.image = base64.b64encode(el.image).decode('ascii')
    return render_template("site/index.html", data=list, item=items, post=post)
