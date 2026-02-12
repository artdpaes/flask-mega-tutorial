from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

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

def make_post(user, body : str):
    return {"author": user, "body": body}

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        flash("Login requested for user {}, remember_me={}".format(
            form.username.data, form.remember_me.data))
        return redirect("/index")

    return render_template("login.html", title="Sign In", form=form)
