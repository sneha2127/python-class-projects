from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, Flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///task.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = "false"

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET"])
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug = True)