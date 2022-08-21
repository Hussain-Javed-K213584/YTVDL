from flask import Flask, render_template, session, request
from flask_mail import Mail

secret_key = Flask.secret_key()
print(secret_key)