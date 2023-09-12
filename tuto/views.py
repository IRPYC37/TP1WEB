from .app import app
from flask import render_template

@app.route("/")
def home():
    return render_template(
        "home.html",
        title= "HELLO WORLD !",
        names=["Pierre", "Paul", "Corinne"])