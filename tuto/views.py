from .app import app
from flask import render_template

@app.route("/")
def home():
    return render_template(
        "home.html",
        title= "HELLO WORLD !",
        names=["Pierre", "Paul", "Corinne"])
    
@app.route("/test")
def test():
    return render_template(
        "test.html",
        title= "HELLO WORLD !",
        message="C'est un TEST")