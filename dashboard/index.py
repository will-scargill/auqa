from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

@app.route("/myroute")
def mypage():
    return "Hello. I'm a route!"

if __name__ == "__main__":
    app.run()
