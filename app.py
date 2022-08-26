from flask import Flask, render_template, session, request, redirect, send_file
from pytube import YouTube
from io import BytesIO
from cs50 import SQL
from datetime import datetime
import os


# Set flask app
app = Flask("__name__")

# Makes sure templates auto reload
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Connect to database
# For heroku
# uri = os.getenv("history.db")
# print(uri)
# if uri.startswith("postgres://"):
#     uri = uri.replace("postgres://", "postgresql://")
# db = SQL(uri)

# The following app with test to download youtube videos

# URL: https://www.youtube.com/watch?v=ndsaoMFz9J4&ab_channel=Markiplier

# Dont route to '/' for post request
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=['GET', 'POST'])
def result():
    link = request.form.get("link")
    if not link or link == "":
        return render_template("apology.html")
    try:
        yt = YouTube(link)
    except:
        return render_template("apology.html")
    return render_template("result.html", title=yt.title, author=yt.author, image=yt.thumbnail_url, link=link)

@app.route("/download", methods=['GET', 'POST'])
def get_video():
    if request.method == "POST":
        link = request.form.get("download-button")
        quality = request.form.get("quality")
        print(quality)
        yt = YouTube(link)
        print(link)
        if quality[-1] == "p":
            # update_db(yt.title, yt.author, link, "mp4")
            yt = yt.streams.filter(progressive=True, file_extension='mp4')
            yt = yt.get_by_resolution(quality)
            buffer = BytesIO() # Use buffer to not to download file on server
            yt.stream_to_buffer(buffer)
            buffer.seek(0)
            return send_file(buffer, as_attachment=True, download_name=yt.title + ".mp4", mimetype="video/mp4")
        elif quality == "mp3":
            # update_db(yt.title, yt.author, link, "mp3")
            yt = yt.streams.filter(progressive=True, file_extension='mp4')
            yt = yt.get_highest_resolution()
            buffer = BytesIO() # Use buffer to not to download file on server
            yt.stream_to_buffer(buffer)
            buffer.seek(0)
            return send_file(buffer, as_attachment=True, download_name=yt.title + ".mp3", mimetype="audio/mp3")
    return redirect("/")


# def update_db(title, author, url, file_type):
#     timestamp = datetime.now()
#     db.execute("INSERT INTO history(url, title, author, file_type, timestamp) VALUES (?, ?, ?, ?, ?)", url, title, author, file_type, timestamp)