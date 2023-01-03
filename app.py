from flask import Flask, url_for, render_template, send_from_directory
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient()


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



if __name__ == '__main__':
    app.run()
