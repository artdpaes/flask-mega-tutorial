from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
    user = make_user("Fulano")

    posts = [
        make_post(make_user("John"), "Beautiful day in Portland!"),
        make_post(make_user("Susan"), "The Avengers movie was so cool!")
    ]

    return render_template("index.html", title="Home", user=user, posts=posts)

def make_user(username : str):
    return {"username": username}

def make_post(user, body):
    return {"author": user, "body": body}
