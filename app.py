from flask import Flask, url_for, render_template, send_from_directory
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient()

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




"""
Static Pages

"""

@app.route('/')
@app.route('/index.html')
def main():  # put application's code here
    return render_template("index.html")

@app.route('/projects.html')
def projects():  # put application's code here
    return render_template("projects.html")

@app.route('/outreach.html')
def outreach():  # put application's code here
    return render_template("outreach.html")

@app.route('/fund.html')
def fund():  # put application's code here
    return render_template("fund.html")


# Uncomment the following if testing internalIndex.html with local MongoDB
'''
@app.route('/')
@app.route('/internalIndex.html', methods = ['GET'])
def internalIndex():  # put application's code here
    return render_template("internalIndex.html", person = person) 
'''

if __name__ == '__main__':
    app.run()
