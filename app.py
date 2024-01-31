from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


# Main/Home page route
@app.route("/")
def hello_world():
    return render_template("index.html")
