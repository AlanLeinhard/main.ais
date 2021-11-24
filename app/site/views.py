from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

from app import db
from app.models import Item, Post

bp = Blueprint("site", __name__)


@bp.route("/")
def index():
    """Show all the posts, most recent first."""
    items = Item.query.order_by(Item.created).all()
    post = Post.query.order_by(Post.created).all()
    return render_template("site/index.html", item=items, post=post)











# @bp.route("/create", methods=("GET", "POST"))
# # @login_required
# def create():
#     """Create a new post for the current user."""
#     if request.method == "POST":
#         title = request.form["title"]
#         body = request.form["body"]
#         error = None

#         if not title:
#             error = "Title is required."

#         if error is not None:
#             flash(error)
#         else:
#             db.session.add(Post(title=title, body=body, author=g.user))
#             db.session.commit()
#             return redirect(url_for("site.index"))

#     return render_template("site/create.html")


# @bp.route("/<int:id>/update", methods=("GET", "POST"))
# # @login_required
# def update(id):
#     """Update a post if the current user is the author."""
#     post = get_post(id)

#     if request.method == "POST":
#         title = request.form["title"]
#         body = request.form["body"]
#         error = None

#         if not title:
#             error = "Title is required."

#         if error is not None:
#             flash(error)
#         else:
#             post.title = title
#             post.body = body
#             db.session.commit()
#             return redirect(url_for("site.index"))

#     return render_template("site/update.html", post=post)


# @bp.route("/<int:id>/delete", methods=("POST",))
# # @login_required
# def delete(id):
#     """Delete a post.
#     Ensures that the post exists and that the logged in user is the
#     author of the post.
#     """
#     post = get_post(id)
#     db.session.delete(post)
#     db.session.commit()
#     return redirect(url_for("site.index"))