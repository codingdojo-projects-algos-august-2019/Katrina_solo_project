from flask import render_template, redirect, request, session
from config import app, db
from models import User, Tour


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/edit")
def edit():
    is_valid = Tour.validate_edit(request.form)
    if is_valid:
        print(request.form)
        edit_tour = Tour.query.get(session["tour_id"])
        print("*"*40)
        print(edit_tour)
        edit.artist= request.form['artist']
        edit.date= request.form['date']
        edit.city= request.form['city']
        db.session.commit()
        return redirect("/")
    else:
        return render_template("edit.html")


# @app.route("/edit")
# def edit(id):
#     if 'user_id' not in session:
#         return redirect("/")
#     else:
#         logged_in = Tour.query.get(session["session_id"])
#         print("*"*30)
#         return render_template("edit.html", user=logged_in)



# @app.route("/subscribe")
# def subscribe():
#     is_valid = User.validate_subscription(request.form)
#     if is_valid:
#         new_user = User.add_new_user(request.form)
#         session["user_id"] = new_user.id
#         return redirect("/")
#     else:
#         return redirect("/")
