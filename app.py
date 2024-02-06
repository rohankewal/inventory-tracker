from flask import Flask, render_template, request
import sqlite3
from werkzeug.security import generate_password_hash

app = Flask(__name__)


# TODO: Setup database for creating and logging in users
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute(
    """CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
    )"""
)


# Main/Home page route
@app.route("/")
def index():
    name = request.args.get("name", "Guest")
    return render_template("index.html", first_name=name)


if __name__ == "__main__":
    app.run(debug=True)
