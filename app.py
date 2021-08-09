import os
import ssl
from flask import Flask, flash, render_template, redirect, request, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app, ssl_cert_reqs=ssl.CERT_NONE)

@app.route("/")
@app.route("/get_deals")
def get_deals():
    deals = mongo.db.deals.find()
    return render_template("deals.html", deals=deals)


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/registration")
def registration():
    return render_template("registration.html")


@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
