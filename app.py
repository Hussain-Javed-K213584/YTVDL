from asyncore import file_wrapper
from crypt import methods
from flask import Flask, render_template, session, request, redirect
from flask_mail import Mail
from pytube import YouTube
import moviepy.editor as mp

# Set flask app
app = Flask("__name__")

# Makes sure templates auto reload
app.config["TEMPLATES_AUTO_RELOAD"] = True

# The following app with test to download youtube videos

# Dont rout to '/' for post request
@app.route("/video-download")
def index():
    return render_template("index.html")

def get_video(url):
    video_obj = YouTube(url)
    video_obj.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download('./Downloads')


