from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


# Main/Home page route
@app.route("/")
def hello_world():
    name = request.args["name"]
    return render_template("index.html", first_name=name)


if __name__ == "__main__":
    app.run(debug=True)
