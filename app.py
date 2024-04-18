from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/request-sitter")
def requestsitter():
  return render_template("requestsitter.html")

@app.route("/view-requests")
def viewrequests():
  return render_template("viewrequests.html")

@app.route("/contact-us")
def contactus():
  return render_template("contactus.html")

@app.route("/FAQ")
def faq():
  return render_template("faq.html")

@app.route("/login")
def login():
  return render_template("login.html")

if __name__ == "__main__":
  app.run()