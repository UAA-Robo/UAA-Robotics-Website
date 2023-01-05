from flask import Flask, url_for, render_template, send_from_directory, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from pymongo import MongoClient

                                                   ##USE 'FLASK RUN' COMMAND WITHIN YOUR VENV TO RUN APP##

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"



'''
Uncomment the following if testing with local MongoDB uaa-robo downloaded from 
https://drive.google.com/drive/folders/1AdAEVCsk90r3HB74M-stUP_JhE84dCHs?usp=sharing
There is also more to uncomment futher below and  in internalIndex.html
'''

'''
client = MongoClient('localhost', 27017) #For testing with local mongo db. 27017 is the proper port
db = client['uaa-robo'] #Same as db = client.uaa-robo (but python doesn't like the uaa-robo format)
person = db.Person
'''

Session(app)



"""
Static Pages

"""

@app.route('/', methods=["GET"])
@app.route('/index.html')
def main():  # put application's code here
    return render_template("index.html")

@app.route('/projects.html', methods=["GET"])
def projects():  # put application's code here
    return render_template("projects.html")

@app.route('/outreach.html', methods=["GET"])
def outreach():  # put application's code here
    return render_template("outreach.html")

@app.route('/fund.html', methods=["GET"])
def fund():  # put application's code here
    return render_template("fund.html")


# Uncomment the following if testing internalIndex.html with local MongoDB
'''
@app.route('/')
@app.route('/internalIndex.html', methods = ['GET'])
def internalIndex():  # put application's code here
    return render_template("internalIndex.html", person = person) 
'''