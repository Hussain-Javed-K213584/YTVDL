from flask import Flask, render_template, session, request, redirect, send_file
from pytube import YouTube
from io import BytesIO

# Set flask app
app = Flask("__name__")

# Makes sure templates auto reload
app.config["TEMPLATES_AUTO_RELOAD"] = True

# The following app with test to download youtube videos

# URL: https://www.youtube.com/watch?v=ndsaoMFz9J4&ab_channel=Markiplier

# Dont route to '/' for post request
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=['GET', 'POST'])
def result():
    link = request.form.get("link")
    yt = YouTube(link)
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
            yt = yt.streams.filter(progressive=True, file_extension='mp4')
            yt = yt.get_by_resolution(quality)
            buffer = BytesIO() # Use buffer to not to download file on server
            yt.stream_to_buffer(buffer)
            buffer.seek(0)
            return send_file(buffer, as_attachment=True, download_name=yt.title + ".mp4", mimetype="video/mp4")
        elif quality == "mp3":
            yt = yt.streams.filter(progressive=True, file_extension='mp4')
            yt = yt.get_highest_resolution()
            buffer = BytesIO() # Use buffer to not to download file on server
            yt.stream_to_buffer(buffer)
            buffer.seek(0)
            return send_file(buffer, as_attachment=True, download_name=yt.title + ".mp3", mimetype="audio/mp3")
    return redirect("/")


