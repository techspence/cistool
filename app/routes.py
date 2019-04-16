from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/base_control')
def base_control():
    return render_template('base_control.html')


@app.route('/login')
def login():
    return render_template('login.html')