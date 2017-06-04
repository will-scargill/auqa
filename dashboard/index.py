from flask import Flask, render_template, send_from_directory
import auth
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

@app.route("/dashboard")
@auth.requires_auth
def say_hi():
    return render_template("dashboard.html.j2")

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
