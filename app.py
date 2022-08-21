from flask import Flask, render_template, session, request, redirect
from flask_mail import Mail

# Set flask app
app = Flask("__name__")

# Configure secret key for sessions
app.secret_key = '06a8237a129aac9be5c85528626dfe946cfe6a3079035cd46b2c8bfbcf9e9ee0'

# The following app with test to download youtube videos
@app.route("/")
def index():
    return render_template("index.html")
