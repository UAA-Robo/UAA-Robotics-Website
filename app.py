from flask import Flask, url_for, render_template, send_from_directory


app = Flask(__name__)


@app.route('/')
def main():  # put application's code here
    return "Empty flask app"

@app.route('/dev/')
def dev_main():
    return "Hello!"


if __name__ == '__main__':
    app.run()
