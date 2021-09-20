import os
import json
from flask import Flask, render_template, url_for, request, redirect
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
from pydantic import ValidationError
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


@app.route("/")
@app.route("/index/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        package = {
                'senderName': request.form.get('Sender_Name'),
                'senderAddress': request.form.get('Sender_Address'),
                'senderCity': request.form.get('Sender_City'),
                'senderCountry': request.form.get('Sender_Country'),
                'recipientName': request.form.get('Recipient_Name'),
                'recipientAddress': request.form.get('Recipient_Address'),
                'recipientCity': request.form.get('Recipient_City'),
                'recipientCountry': request.form.get('Recipient_Country'),
                'despatchDate': request.form.get('Date'),
                'value': request.form.get('Value'),
                'content': request.form.get('Content'),
                'insuranceProvived': request.form.get('Insurance'),
                'trackingNumber': request.form.get('Tracking_Number')
            }
        mongo.db.Package.insert_one(package)
        print('inserted')
        return redirect(url_for('orders'))
    return render_template("index.html")


@app.route("/Orders/<order>", methods=["GET, POST"])
def orders(order):
    if request.method == "POST":
        order = mongo.db.Package.find_one({"_id": ObjectId(order)})
        return render_template("orders.html", order = order)
  

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
