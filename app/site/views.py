from flask import Blueprint, render_template

from app.models import Item, Post

bp = Blueprint("site", __name__)


@bp.route("/")
def index():
    """Show all the posts, most recent first."""
    items = Item.query.order_by(Item.created).all()
    post = Post.query.order_by(Post.created).all()
    return render_template("site/index.html", item=items, post=post)
