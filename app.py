import os
import json
from flask import Flask, render_template, url_for, request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        sender = {
            'senderName': request.form.get('Sender_Name'),
            'address': request.form.get('Sender_Address'),
            'city': request.form.get('Sender_City'),
            'country': request.form.get('Sender_Country')
        }
        mongo.db.Package.insert_one(sender)
        
    return render_template("index.html")


@app.route("/Orders/", methods=["GET", "POST"])
def orders():

    return render_template("orders.html")



if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)