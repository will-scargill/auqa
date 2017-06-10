from flask import Flask, render_template, send_from_directory
import sqlite3
import time
import datetime

# Setup SQLite Database
conn = sqlite3.connect("database.db", check_same_thread=False)
c = conn.cursor()

app = Flask(__name__)

@app.route("/")
def dashboard():
    c.execute("SELECT temperature, pressure, humidity, timestamp FROM `data` ORDER BY timestamp DESC LIMIT 1")
    current = c.fetchall()[0]
    c.execute("SELECT temperature, pressure, humidity, timestamp FROM `data` WHERE timestamp >= datetime('now', '-1 day') ORDER BY timestamp ASC")
    history = c.fetchall()
    #log(current)
    return render_template("dashboard.html.j2", current=current, history=history);

@app.route("/assets/js/<path:path>")
def send_js(path):
    return send_from_directory("assets/js", path)

@app.route("/assets/css/<path:path>")
def send_css(path):
    return send_from_directory("assets/css", path)

@app.route("/assets/fonts/<path:path>")
def send_fonts(path):
    return send_from_directory("assets/fonts", path)

def log(message):
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S %d/%m/%Y')
    print("[" + st + "] ", message)

if __name__ == "__main__":
    app.run()
