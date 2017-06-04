from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"
  
@app.route("/infomation")
def infomation():
    return "This is a website for the plant system we are making"
    
@app.route("/html")
def html():
    return app.send_static_file("index.html")

if __name__ == "__main__":
    app.run()
