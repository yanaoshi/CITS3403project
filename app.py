from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/request-sitter")
def requestsitter():
  return render_template("requestsitter.html")

if __name__ == "__main__":
  app.run()