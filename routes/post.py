from flask import Blueprint, render_template, redirect, url_for, request, current_app # New imports added
from sqlmodel import Session, select
from models.post import Post

post_pages = Blueprint("posts", __name__)

@post_pages.get("/post/<string:title>")
def display_post(title):
    content = "..." # How do we get the content?
    return render_template("post.html", title=title, content=content)

@post_pages.route("/post/", methods=["GET", "POST"])
def create_post():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        with Session(current_app.engine) as session:
            session.add(Post(title=title, content=content))
            session.commit()
        return redirect(url_for("display_post", title=title))
    return render_template("new_post.html")

