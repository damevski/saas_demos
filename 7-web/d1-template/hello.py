from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<user_name>/<user_age>')
def user(user_name,user_age):
    return render_template('user.html', name=user_name, age=user_age)
