from flask import Flask, render_template, send_from_directory
import sqlite3

# Setup SQLite Database
conn = sqlite3.connect("../database.db")
c = conn.cursor()

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

@app.route("/dashboard")
def dashboard():
    c.execute("SELECT * FROM data ORDER BY date ASC LIMIT 50")
    output = c.fetchall()
    return render_template("dashboard.html.j2", {
        weatherdata: output
    });

@app.route("/assets/js/<path:path>")
def send_js(path):
    return send_from_directory("assets/js", path)

@app.route("/assets/css/<path:path>")
def send_css(path):
    return send_from_directory("assets/css", path)

@app.route("/assets/fonts/<path:path>")
def send_fonts(path):
    return send_from_directory("assets/fonts", path)

if __name__ == "__main__":
    app.run()
