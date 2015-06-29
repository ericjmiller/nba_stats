from flask import render_template, url_for

from . import app

@app.route('/')
def index():
    return template('index.html')
