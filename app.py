import os
import json
from flask import Flask, render_template, url_for, request, redirect
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
from pydantic import ValidationError
import binascii
import datetime
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
        value = float(request.form.get('Value'))
        print(value)
        despatchDate = request.form.get('Date')
        recipientCountry = request.form.get('Recipient_Country').upper()
        insuranceProvided = request.form.get('Insurance')
        print(insuranceProvided)
        insuranceCharge = 0.00
        trackingNumber = binascii.b2a_hex(os.urandom(15))
        print(trackingNumber)
        existing_trackingNumber = mongo.db.Package.find_one(
            {"trackingNumber": "trackingNumber"}
        )
        acceptedAt = datetime.datetime.now()
        print(acceptedAt)
        if value < 10000 and existing_trackingNumber != True:
            print('value')
            if insuranceProvided == 'True':
                print('true')
                insuranceProvided = 'Yes'
                print('yes')
                if recipientCountry == 'GB':
                    print(recipientCountry)
                    insuranceCharge = round(value * 0.01, 3)
                    print(insuranceCharge)
                if recipientCountry == 'DE' or recipientCountry == 'NE' or recipientCountry == 'FR' or recipientCountry == 'BE':
                    insuranceCharge = round(value * 0.015, 3)
                else:
                    insuranceCharge = round(value * 0.04, 3)   
        else:
            insuranceCharge = 0.00
            insuranceProvided == 'False'
        if  insuranceCharge < 9.00:
            insuranceCharge 9.00
        ipt = round(insuranceCharge * 0.12, 3)

        package = {
            'senderName': request.form.get('Sender_Name'),
            'senderAddress': request.form.get('Sender_Address'),
            'senderCity': request.form.get('Sender_City'),
            'senderCountry': request.form.get('Sender_Country'),
            'recipientName': request.form.get('Recipient_Name'),
            'recipientAddress': request.form.get('Recipient_Address'),
            'recipientCity': request.form.get('Recipient_City'),
            'recipientCountry': recipientCountry,
            'value': value,
            'content': request.form.get('Content'),
            'insuranceProvived': insuranceProvided,
            'insuranceCharge': insuranceCharge,
            'ipt': ipt,
            'trackingNumber': trackingNumber,
            'despatchDate': despatchDate,
            #'orderURL': orderURL,
            'acceptedAt': acceptedAt
        }
        order = mongo.db.Package.insert_one(package)
        return redirect(url_for('orders', order=order.inserted_id))

    return render_template("index.html")


@app.route("/Orders/<order>", methods=["GET"])
def orders(order):

    order = mongo.db.Package.find_one({"_id": ObjectId(order)})
    return render_template("orders.html", order=order)


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
