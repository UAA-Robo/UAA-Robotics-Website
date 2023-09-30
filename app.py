import configparser
from flask import Flask, url_for, render_template, send_from_directory, redirect, render_template, request
from flask_session import Session
from tempfile import mkdtemp
from pymongo import MongoClient
# DELETE ME
from bson.objectid import ObjectId #For working with PyMongo object Ids

##USE 'FLASdK RUN' COMMAND WITHIN YOUR VENV TO RUN APP##

app = Flask(__name__)


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

# Read the INI file
config = configparser.ConfigParser()
config.read("config.ini")




#This connects to our Atlas MongoDB. Your IP Adress will need to be added to the Newtork Access List on the Atlas website
client = MongoClient(config["PROD"]["DB_URI"])
db = client["uaa-robo"] #Same as db = client.uaa-robo (but python doesn't like the uaa-robo format)
people = db.Person
tasks = db.Task
logs = db.Log

#Alternative test customer db to use:
'''
db = client["sample_analytics"] #Alternative testing
people = db.customers
''' 

Session(app)


"""
Static Pages

"""

@app.route("/")
def main():  # put application's code here
    return render_template("home.html")

@app.route("/projects", methods=["GET"])
def projects():  # put application's code here
    return render_template("projects.html")

@app.route("/outreach", methods=["GET"])
def outreach():  # put application's code here
    return render_template("outreach.html")

@app.route("/fund", methods=["GET"])
def fund():  # put application's code here
    return render_template("fund.html")


"""
Dynamic Pages

"""

@app.route("/task_listing", methods = ["GET", "POST"])
def task_listing():  # put application's code here
    if request.method=="GET":
        options = ["open", "in-progress", "stalled", "complete", "recurring"]
        return render_template("task_listing.html", people = people, tasks = tasks, options=options)
    ID = request.form.get("ObjectID")
    updatedStatus = request.form.get("Status")

    return redirect("task_listing")


@app.route("/tasks/<string:id>", methods = ["GET"])
def task(id):  

    singleTask = tasks.find_one(ObjectId(id))

    return render_template("task.html", singleTask = singleTask, logs=logs, people = people) 
