# YouTube Video Downloader
#### Video Demo: [YTVDL - A CS50x Project](https://www.youtube.com/watch?v=TWzjLfXKdio&ab_channel=HussainJaved)
#### Description: 
This is my final project for CS50x. The name of the project is YTVDL or YouTube video downloader.
The name tells itself that the project is related downloading videos from YouTube and yes that is correct.
## How did I go on to implement this?
I started searching for ways to download videos from YouTube and sometimes download music from YouTube in an .mp3 format.
Almost every website I visited had annoying ads and they were obviously tracking me, so I thought, why not I make a YouTube video
downloader myself? So I went on to Google, searched for a way to use python and flask to download videos from YouTube adn Voila!
[Pytube](https://pytube.io/en/latest/), a light weight open source module of python which had the ability to use a YouTube video URL
and download that video into multiple qualities.

## The app itself
The application consist of the main app.py where I am importing multiple familiar libraries but there is one called [io](https://docs.python.org/3/library/io.html),
more on that later. The structure of my directory is something like this:
```bash
.
├── Database
│   └── history.db
├── OpenSans
│   ├── OpenSans-Bold.ttf
│   ├── OpenSans-BoldItalic.ttf
│   ├── OpenSans-ExtraBold.ttf
│   ├── OpenSans-ExtraBoldItalic.ttf
│   ├── OpenSans-Italic.ttf
│   ├── OpenSans-Light.ttf
│   ├── OpenSans-LightItalic.ttf
│   ├── OpenSans-Medium.ttf
│   ├── OpenSans-MediumItalic.ttf
│   ├── OpenSans-Regular.ttf
│   ├── OpenSans-SemiBold.ttf
│   └── OpenSans-SemiBoldItalic.ttf
├── Procfile
├── README.md
├── __pycache__
│   └── app.cpython-38.pyc
├── app.py
├── requirements.txt
├── static
│   ├── falcon.png
│   ├── script.js
│   └── style.css
├── templates
│   ├── apology.html
│   ├── index.html
│   ├── layout.html
│   ├── result.html
│   └── video.html
└── test.txt
```
Yes, a lot of files.
### Templates
Let's start with the templates directory. I created a layout.html in which I added a header and some css to it using my personal stylesheet. I then used
```jinja``` syntax to template my ```layout.html``` file into multiple other files. I then created an index.html file which would route to "/", which is the 
root of my web application. I created three other HTML files called ```result.html```, ```video.html```, ```apology.html```. Every HTML file used the ```layout.html``` template.

### Index.html
Let's start with index.html. The file consist of an input text field which requires a YouTube URL. Beside the text field is a button which was created using bootstrap.
I then borrowed the code from [Codepen](https://codepen.io/Tipue/pen/NzpeoN) to make the input field more repsonsive when viewing the web app from a smartphone.
### Result.html
The result.html would be rendered once the user clicks on the Download button on the index.html page. The result.html will show the user with the details
of the video he/she requested to download. The details include:
- Video Title
- Video author
- Video Thumbnail
The page also contains a download button and a quality dropdown menu having three options:
- 720p
- 360p
- mp3<br>
Where mp3 is used to download only the audio of the video, this option was specifically for music videos.

### Apology.html
This page generates a grumpy cat image generated using the [Memegen](https://github.com/jacebrowning/memegen) API found on GitHub. This page is rendered whenever the
user fails to provide with a valid YouTube URL or does not write a URL at all.

### App.py
Let's talk about the main file of our web app, app.py. We can see a lot of module imports, here the most important one is [Pytube](https://pytube.io/en/latest/) YouTube module which is used when we want to pass a YouTube URL into it. It then returns us a YouTube object which can be used to download the YouTube video.
I used sqlite3 for database in this web app and what that database is storing is the history of downloads made using my web application. The ```@app.route("/")``` renders the ```index.html``` page which then routes to the ```@app.route("/result")``` route and renders the result.html page and once we confirm the quality of the 
video which we want to download we are then routed to the ```@app.route("/download")``` route and the downloading begins. Our main work handled in the ```get_video()``` function. We fetch a YouTube URL from the form with a ```POST``` request and also the quality of that video. Once we have both the URL and the quality we then begin by creating the YouTube object using the ```YouTube()``` module from [Pytube](https://pytube.io/en/latest/). Then there is an if condition to check if the user requested to download a video or an audio file. If the last character of the string is 'p' then we know the user wants to download a video. We filter
out the streams we want where we make sure that the stream is progressive so that we get both the audio and video in a single .mp4 file and we specify the quality
of the video by using the ```get_by_resolution(quality)``` method. Once all this is complete we use the python [io](https://docs.python.org/3/library/io.html) library 
to make sure that we are not downloading the file on our server but on the user's desktop or smartphone. We stream the video to the buffer and use the ```send_file()``` function to send the user the file he wished to download.
### Update_db()
The update_db uses [cs50](https://pypi.org/project/cs50/) library to execute SQL commands, more specifically, sqlite3 commands to add data in out history.db database.
