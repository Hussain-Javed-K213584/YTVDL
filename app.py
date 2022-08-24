from flask import Flask, render_template, session, request, redirect
from pytube import YouTube
import moviepy.editor as mp

# Set flask app
app = Flask("__name__")

# Makes sure templates auto reload
app.config["TEMPLATES_AUTO_RELOAD"] = True

# The following app with test to download youtube videos

# URL: https://www.youtube.com/watch?v=Mz97sjRMSzg&ab_channel=Radixerus

# Dont route to '/' for post request
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=['GET', 'POST'])
def result():
    link = request.form.get("link")
    yt = YouTube(link)
    return render_template("result.html", title=yt.title, author=yt.author, image=yt.thumbnail_url)


