from flask import render_template, redirect, request, session
from config import app, db
from models import User, Tour


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/subscribe")
def subscribe():
    is_valid = User.validate_subscription(request.form)
    if is_valid:
        new_user = User.add_new_user(request.form)
        session["user_id"] = new_user.id
        return redirect("/")
    else:
        return redirect("/")
