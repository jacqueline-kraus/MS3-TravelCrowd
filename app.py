import os
import ssl
from functools import wraps
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

if os.path.exists("env.py"):
    mongo = PyMongo(app, ssl_cert_reqs=ssl.CERT_NONE)
else:
    mongo = PyMongo(app)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            flash("You need to be logged in to view this.")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/get_deals")
def get_deals():
    deals = mongo.db.deals.find().sort("_id", -1)
    return render_template("deals.html", deals=deals)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    deals = list(mongo.db.deals.find({"$text": {"$search": query}}))
    return render_template("deals.html", deals=deals)


@app.route("/registration", methods=["GET", "POST"])
def registration():
    if "user" not in session:
        # registration is the same as in CI videos
        if request.method == "POST":
            # check if username already exists in database
            existing_user = mongo.db.users.find_one(
                {"username": request.form.get("username").lower()})

            if existing_user:
                flash("Username already exists")
                return redirect(url_for("registration"))

            register = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(
                    request.form.get("password"))
            }
            mongo.db.users.insert_one(register)

            # put the new user into 'session' cookie
            session["user"] = request.form.get("username").lower()
            flash("Registration Successful!")
            return redirect(url_for("profile", username=session["user"]))
        return render_template("registration.html")

    # user is already logged-in, direct them to their profile
    return redirect(url_for("profile", username=session["user"]))


@app.route("/login", methods=["GET", "POST"])
def login():
    if "user" not in session:
        # only if there isn't a current session["user"]
        if request.method == "POST":
            # check if username exists in db
            existing_user = mongo.db.users.find_one(
                {"username": request.form.get("username").lower()})

            if existing_user:
                # ensure hashed password matches user input
                if check_password_hash(existing_user["password"],
                                       request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    return redirect(url_for(
                        "profile", username=session["user"]))
                else:
                    # invalid password match
                    flash("Incorrect Username and/or Password")
                    return redirect(url_for("login"))
            else:
                # username doesn't exist
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        return render_template("login.html")

    # user is already logged-in, direct them to their profile
    return redirect(url_for("profile", username=session["user"]))


@app.route("/profile/<username>", methods=["GET", "POST"])
@login_required
def profile(username):
    if session["user"].lower() == username.lower():
        # find the session.user
        user = mongo.db.users.find_one({"username": username})
        # find only deals created by session.user
        deals = list(mongo.db.deals.find({"created_by": username}))
        return render_template("profile.html", user=user, deals=deals)
    return redirect(url_for("login"))


@app.route("/logout")
@login_required
def logout():
    # remove user from session cookies
    flash("Successfully logged out!")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/create_deal", methods=["GET", "POST"])
@login_required
def create_deal():
    # add a new deal
    if request.method == "POST":
        deal = {
            "deal_name": request.form.get("deal_name"),
            "destination_country": request.form.get("destination_country"),
            "destination_city": request.form.get("destination_city"),
            "price": request.form.get("price"),
            "description": request.form.get("description"),
            "departure_airport": request.form.get("departure_airport"),
            "start_date": request.form.get("start_date"),
            "end_date": request.form.get("end_date"),
            "booking_link": request.form.get("booking_link"),
            "created_by": session["user"]
        }
        mongo.db.deals.insert_one(deal)
        flash("Deal successfully published!")
        return redirect(url_for("get_deals"))

    return render_template("create_deal.html")


@app.route("/edit_deal/<deal_id>", methods=["GET", "POST"])
@login_required
def edit_deal(deal_id):
    deal = mongo.db.deals.find_one({"_id": ObjectId(deal_id)})
    if session["user"].lower() == deal["created_by"].lower():
        if request.method == "POST":
            submit = {
                "deal_name": request.form.get("deal_name"),
                "destination_country": request.form.get("destination_country"),
                "destination_city": request.form.get("destination_city"),
                "price": request.form.get("price"),
                "description": request.form.get("description"),
                "departure_airport": request.form.get("departure_airport"),
                "start_date": request.form.get("start_date"),
                "end_date": request.form.get("end_date"),
                "booking_link": request.form.get("booking_link"),
                "created_by": session["user"]
            }
            mongo.db.deals.update({"_id": ObjectId(deal_id)}, submit)
            flash("Deal successfully updated!")
            return redirect(url_for("get_deals"))

        return render_template("edit_deal.html", deal=deal)

    flash("You are not allowed to edit this deal.")
    return redirect(url_for("get_deals"))


@app.route("/delete_deal/<deal_id>")
@login_required
def delete_deal(deal_id):
    deal = mongo.db.deals.find_one({"_id": ObjectId(deal_id)})
    if session["user"].lower() == deal["created_by"].lower():
        mongo.db.deals.remove({"_id": ObjectId(deal_id)})
        flash("Deal successfully deleted!")
        return redirect(url_for("get_deals"))

    flash("You have no permission to delete this deal")
    return redirect(url_for("get_deals"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
