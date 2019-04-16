from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/manage_controls')
def manage_controls():
    return render_template('manage_controls.html')


@app.route('/login')
def login():
    return render_template('login.html')