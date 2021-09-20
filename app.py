import os
import json
from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)


@app.route("/")
def index():
    #if request.method == "POST":
    return render_template("index.html")


@app.route("/Orders/", methods=["GET"])
def orders():

    return render_template("orders.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)